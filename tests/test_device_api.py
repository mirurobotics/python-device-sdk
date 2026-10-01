from __future__ import annotations

import sys
import json
import threading
from typing import Any, List, Union, Iterator, Optional
from pathlib import Path
from unittest import mock
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from typing_extensions import override

import httpx
import pytest

from miru_device_sdk import Miru, AsyncMiru, APIConnectionError, AuthenticationError
from miru_device_sdk._types import Omit
from miru_device_sdk.lib.device_api import (
    Discovery,
    DiscoveryFile,
    AgentTransport,
    DiscoveryError,
    DiscoveryTransport,
    AsyncDiscoveryTransport,
    discovery_for,
    read_discovery,
    resolve_transport,
    default_discovery_file,
)

from .utils import update_env


@pytest.fixture(autouse=True)
def no_retry_delay() -> Iterator[None]:
    with mock.patch("miru_device_sdk._base_client.BaseClient._calculate_retry_timeout", return_value=0):
        yield


def write_discovery(path: Path, port: int, token: str) -> None:
    path.write_text(json.dumps({"port": port, "token": token}))


class TestReadDiscovery:
    def test_valid(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        write_discovery(path, 43210, "tok")
        assert read_discovery(str(path)) == Discovery(port=43210, token="tok")

    def test_ignores_other_fields(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        path.write_text('{"port": 43210, "token": "tok", "pid": 7}')
        assert read_discovery(str(path)) == Discovery(port=43210, token="tok")

    def test_missing(self, tmp_path: Path) -> None:
        with pytest.raises(DiscoveryError, match="not found"):
            read_discovery(str(tmp_path / "absent.json"))

    @pytest.mark.parametrize(
        "contents, message",
        [
            ("{", "not valid JSON"),
            ("[]", "not a JSON object"),
            ('{"token": "t"}', "invalid port"),
            ('{"port": 0, "token": "t"}', "invalid port"),
            ('{"port": 65536, "token": "t"}', "invalid port"),
            ('{"port": true, "token": "t"}', "invalid port"),
            ('{"port": "80", "token": "t"}', "invalid port"),
            ('{"port": 80, "token": ""}', "invalid token"),
            ('{"port": 80}', "invalid token"),
        ],
    )
    def test_invalid(self, tmp_path: Path, contents: str, message: str) -> None:
        path = tmp_path / "device-api.json"
        path.write_text(contents)
        with pytest.raises(DiscoveryError, match=message):
            read_discovery(str(path))


class TestResolveTransport:
    def test_default_is_unix_off_windows(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "linux")
        assert resolve_transport(None) is AgentTransport.UNIX
        assert resolve_transport("") is AgentTransport.UNIX

    def test_default_is_tcp_on_windows(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "win32")
        assert resolve_transport(None) is AgentTransport.TCP

    def test_explicit(self) -> None:
        assert resolve_transport("tcp") is AgentTransport.TCP
        assert resolve_transport(" UNIX ") is AgentTransport.UNIX

    def test_invalid(self) -> None:
        with pytest.raises(ValueError, match="agent_transport"):
            resolve_transport("pipe")


class TestDefaultDiscoveryFile:
    def test_linux(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "linux")
        assert default_discovery_file() == "/run/miru/device-api.json"

    def test_windows(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "win32")
        monkeypatch.setenv("ProgramData", "D:\\Data")
        path = default_discovery_file()
        assert path.startswith("D:\\Data")
        assert path.replace("\\", "/").endswith("Miru/device-api/device-api.json")


class TestDiscoveryFile:
    def test_reads_once_until_invalidated(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        write_discovery(path, 43210, "old")
        discovery = DiscoveryFile(str(path))
        assert discovery.get() == Discovery(port=43210, token="old")
        write_discovery(path, 43211, "new")
        assert discovery.get().token == "old"
        discovery.invalidate()
        assert discovery.get() == Discovery(port=43211, token="new")

    def test_first_read_failure_raises(self, tmp_path: Path) -> None:
        with pytest.raises(DiscoveryError, match="not found"):
            DiscoveryFile(str(tmp_path / "absent.json")).get()

    def test_keeps_last_values_while_file_is_missing(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        write_discovery(path, 43210, "old")
        discovery = DiscoveryFile(str(path))
        discovery.get()
        path.unlink()  # the agent is restarting
        discovery.invalidate()
        assert discovery.get().token == "old"
        write_discovery(path, 43211, "new")  # still stale, so this read sees the restart
        assert discovery.get().token == "new"

    def test_token_rotated(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        write_discovery(path, 43210, "old")
        discovery = DiscoveryFile(str(path))
        request = httpx.Request("GET", "http://127.0.0.1:43210/", headers={"Authorization": "Bearer old"})
        response = httpx.Response(401, request=request)
        assert not discovery.token_rotated(response)
        write_discovery(path, 43210, "new")
        assert discovery.token_rotated(response)

    def test_discovery_for(self, tmp_path: Path) -> None:
        path = str(tmp_path / "device-api.json")
        assert discovery_for("unix", path, None) is None
        assert discovery_for("tcp", path, "explicit-token") is None
        shared = discovery_for("tcp", path, None)
        assert shared is not None and shared.path == path
        assert discovery_for("tcp", path, None) is shared


Outcome = Union[int, Exception]


class Agent:
    """A scripted agent behind httpx.MockTransport: records requests, answers in order."""

    def __init__(self, path: Path, outcomes: List[Outcome]) -> None:
        self.path = path
        self.outcomes = outcomes
        self.requests: List[httpx.Request] = []

    def __call__(self, request: httpx.Request) -> httpx.Response:
        self.requests.append(request)
        outcome = self.outcomes.pop(0)
        if isinstance(outcome, Exception):
            raise outcome
        return httpx.Response(outcome, json={"status": "ok"}, request=request)

    def client(self, **kwargs: Any) -> Miru:
        discovery = discovery_for("tcp", str(self.path), None)
        assert discovery is not None
        transport = DiscoveryTransport(discovery, httpx.MockTransport(self))
        return Miru(
            agent_transport="tcp",
            discovery_file=str(self.path),
            http_client=httpx.Client(transport=transport),
            **kwargs,
        )

    def sent(self) -> List[str]:
        return [f"{r.url.host}:{r.url.port} {r.headers.get('Authorization')}" for r in self.requests]


class TestClientWithDiscovery:
    def test_sends_to_discovered_port_with_token(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        write_discovery(path, 43210, "tok")
        agent = Agent(path, [200])
        with agent.client() as client:
            assert client.agent.health().status == "ok"
        request = agent.requests[0]
        assert str(request.url) == "http://127.0.0.1:43210/v0.2/health"
        assert request.headers["Host"] == "127.0.0.1:43210"
        assert request.headers["Authorization"] == "Bearer tok"

    def test_401_retries_with_rotated_token(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        write_discovery(path, 43210, "old")
        agent = Agent(path, [200, 401, 200])
        with agent.client() as client:
            client.agent.health()
            write_discovery(path, 43211, "new")  # the agent restarted
            assert client.agent.health().status == "ok"
        assert agent.sent() == [
            "127.0.0.1:43210 Bearer old",
            "127.0.0.1:43210 Bearer old",
            "127.0.0.1:43211 Bearer new",
        ]

    def test_401_with_unchanged_token_is_not_retried(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        write_discovery(path, 43210, "tok")
        agent = Agent(path, [401])
        with agent.client() as client:
            with pytest.raises(AuthenticationError):
                client.agent.health()
        assert len(agent.requests) == 1

    def test_refused_connection_retries_on_new_port(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        write_discovery(path, 43210, "old")
        agent = Agent(path, [200, httpx.ConnectError("refused"), 200])
        with agent.client() as client:
            client.agent.health()
            write_discovery(path, 43211, "new")
            assert client.agent.health().status == "ok"
        assert agent.sent()[2] == "127.0.0.1:43211 Bearer new"

    def test_401_recovers_without_retries(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        write_discovery(path, 43210, "old")
        agent = Agent(path, [200, 401, 200])
        with agent.client(max_retries=0) as client:
            client.agent.health()
            write_discovery(path, 43210, "new")  # restarted on the same port
            with pytest.raises(AuthenticationError):
                client.agent.health()
            assert client.agent.health().status == "ok"
        assert agent.sent()[2] == "127.0.0.1:43210 Bearer new"

    def test_recovers_without_retries(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        write_discovery(path, 43210, "old")
        agent = Agent(path, [200, httpx.ConnectError("refused"), 200])
        with agent.client(max_retries=0) as client:
            client.agent.health()
            path.unlink()  # the agent stopped
            with pytest.raises(APIConnectionError):
                client.agent.health()
            write_discovery(path, 43211, "new")  # and started again
            assert client.agent.health().status == "ok"
        assert agent.sent()[2] == "127.0.0.1:43211 Bearer new"

    def test_missing_file_raises_discovery_error(self, tmp_path: Path) -> None:
        agent = Agent(tmp_path / "absent.json", [])
        with agent.client() as client:
            with pytest.raises(DiscoveryError, match="not running"):
                client.agent.health()
        assert agent.requests == []

    def test_copy_shares_the_discovery(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        write_discovery(path, 43210, "old")
        agent = Agent(path, [httpx.ConnectError("refused"), 200])
        with agent.client(max_retries=0) as client:
            copied = client.copy()
            with pytest.raises(APIConnectionError):
                client.agent.health()
            write_discovery(path, 43211, "new")
            assert copied.agent.health().status == "ok"
        assert agent.sent()[1] == "127.0.0.1:43211 Bearer new"

    def test_explicit_token_skips_discovery(self, tmp_path: Path) -> None:
        requests: List[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(200, json={"status": "ok"}, request=request)

        with Miru(
            agent_transport="tcp",
            discovery_file=str(tmp_path / "absent.json"),
            bearer_token="explicit",
            base_url="http://127.0.0.1:43210/v0.2",
            http_client=httpx.Client(transport=httpx.MockTransport(handler)),
        ) as client:
            client.agent.health()
        assert str(requests[0].url) == "http://127.0.0.1:43210/v0.2/health"
        assert requests[0].headers["Authorization"] == "Bearer explicit"

    def test_unix_socket_sends_no_token(self) -> None:
        requests: List[httpx.Request] = []

        def handler(request: httpx.Request) -> httpx.Response:
            requests.append(request)
            return httpx.Response(200, json={"status": "ok"}, request=request)

        with update_env(MIRU_AGENT_TOKEN=Omit()):
            client = Miru(agent_transport="unix", http_client=httpx.Client(transport=httpx.MockTransport(handler)))
        with client:
            client.agent.health()
        assert "Authorization" not in requests[0].headers
        assert requests[0].url.host == "localhost"

    async def test_async_refused_connection_retries_on_new_port(self, tmp_path: Path) -> None:
        path = tmp_path / "device-api.json"
        write_discovery(path, 43210, "old")
        sent: List[str] = []

        def handler(request: httpx.Request) -> httpx.Response:
            sent.append(f"{request.url.port} {request.headers['Authorization']}")
            if len(sent) == 1:
                write_discovery(path, 43211, "new")  # the agent restarted
                raise httpx.ConnectError("refused")
            return httpx.Response(200, json={"status": "ok"}, request=request)

        discovery = discovery_for("tcp", str(path), None)
        assert discovery is not None
        transport = AsyncDiscoveryTransport(discovery, httpx.MockTransport(handler))
        async with AsyncMiru(
            agent_transport="tcp", discovery_file=str(path), http_client=httpx.AsyncClient(transport=transport)
        ) as client:
            assert (await client.agent.health()).status == "ok"
        assert sent == ["43210 Bearer old", "43211 Bearer new"]


async def test_async_401_recovers_without_retries(tmp_path: Path) -> None:
    path = tmp_path / "device-api.json"
    write_discovery(path, 43210, "old")
    sent: List[str] = []

    def handler(request: httpx.Request) -> httpx.Response:
        sent.append(request.headers["Authorization"])
        status = 401 if request.headers["Authorization"] != "Bearer new" else 200
        return httpx.Response(status, json={"status": "ok"}, request=request)

    discovery = discovery_for("tcp", str(path), None)
    assert discovery is not None
    transport = AsyncDiscoveryTransport(discovery, httpx.MockTransport(handler))
    async with AsyncMiru(
        agent_transport="tcp",
        discovery_file=str(path),
        max_retries=0,
        http_client=httpx.AsyncClient(transport=transport),
    ) as client:
        with pytest.raises(AuthenticationError):
            await client.agent.health()
        write_discovery(path, 43210, "new")  # restarted on the same port
        assert (await client.agent.health()).status == "ok"
    assert sent == ["Bearer old", "Bearer new"]


class FakeAgent:
    """A loopback HTTP server that, like the agent, requires the current bearer token."""

    def __init__(self, discovery_file: Path) -> None:
        self.discovery_file = discovery_file
        self.token = "first"
        self.authorizations: List[Optional[str]] = []
        agent = self

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self) -> None:  # noqa: N802
                agent.authorizations.append(self.headers.get("Authorization"))
                if self.headers.get("Authorization") != f"Bearer {agent.token}":
                    self.send_response(401)
                    self.send_header("WWW-Authenticate", "Bearer")
                    self.send_header("Content-Length", "0")
                    self.end_headers()
                    return
                body = json.dumps({"status": "ok"}).encode()
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            @override
            def log_message(self, format: str, *args: Any) -> None:  # noqa: A002
                pass

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    def publish(self) -> None:
        write_discovery(self.discovery_file, self.server.server_address[1], self.token)

    def restart(self) -> None:
        """Rotate the token, as the agent does on every start."""
        self.token = self.token + "-rotated"
        self.publish()


@pytest.fixture
def fake_agent(tmp_path: Path) -> Iterator[FakeAgent]:
    agent = FakeAgent(tmp_path / "device-api.json")
    agent.publish()
    agent.thread.start()
    try:
        yield agent
    finally:
        agent.server.shutdown()
        agent.server.server_close()


class TestClientOverTcp:
    def test_sync_client_authenticates_and_follows_rotation(self, fake_agent: FakeAgent) -> None:
        with Miru(agent_transport="tcp", discovery_file=str(fake_agent.discovery_file)) as client:
            assert client.agent.health().status == "ok"
            fake_agent.restart()
            assert client.agent.health().status == "ok"
        assert fake_agent.authorizations == ["Bearer first", "Bearer first", "Bearer first-rotated"]

    async def test_async_client_authenticates_and_follows_rotation(self, fake_agent: FakeAgent) -> None:
        async with AsyncMiru(agent_transport="tcp", discovery_file=str(fake_agent.discovery_file)) as client:
            assert (await client.agent.health()).status == "ok"
            fake_agent.restart()
            assert (await client.agent.health()).status == "ok"
        assert fake_agent.authorizations == ["Bearer first", "Bearer first", "Bearer first-rotated"]

    def test_transport_from_env(self, fake_agent: FakeAgent) -> None:
        with update_env(MIRU_AGENT_TRANSPORT="tcp", MIRU_AGENT_DISCOVERY_FILE=str(fake_agent.discovery_file)):
            client = Miru()
        with client:
            assert client.agent.health().status == "ok"

    def test_unix_transport_is_default_off_windows(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "linux")
        with update_env(MIRU_AGENT_TRANSPORT=""):
            client = Miru(socket_path="/tmp/miru-agent-test.sock")
        transport = client._client._transport  # type: ignore[attr-defined]
        assert isinstance(transport, httpx.HTTPTransport)
        assert transport._pool._uds == "/tmp/miru-agent-test.sock"  # type: ignore[attr-defined]
        client.close()

    def test_tcp_transport_is_default_on_windows(self, monkeypatch: pytest.MonkeyPatch) -> None:
        monkeypatch.setattr(sys, "platform", "win32")
        with update_env(MIRU_AGENT_TRANSPORT="", MIRU_AGENT_TOKEN=Omit()):
            client = Miru()
        assert isinstance(client._client._transport, DiscoveryTransport)  # type: ignore[attr-defined]
        client.close()

    def test_tcp_with_explicit_token_uses_plain_transport(self) -> None:
        client = Miru(agent_transport="tcp", bearer_token="explicit")
        transport = client._client._transport  # type: ignore[attr-defined]
        assert isinstance(transport, httpx.HTTPTransport)
        assert transport._pool._uds is None  # type: ignore[attr-defined]
        client.close()

    def test_invalid_transport_is_rejected(self) -> None:
        with pytest.raises(ValueError, match="agent_transport"):
            Miru(agent_transport="pipe")

    def test_supplied_http_client_is_used_as_is(self) -> None:
        http_client = httpx.Client()
        client = Miru(agent_transport="tcp", http_client=http_client)
        assert client._client is http_client
        client.close()
