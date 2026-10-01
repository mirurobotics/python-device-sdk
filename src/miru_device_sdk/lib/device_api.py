"""Reach the Miru Agent's local device API over its Unix socket or loopback TCP.

Over TCP the agent requires `Authorization: Bearer <token>`, which the generated
`bearer_token` option sends. The agent publishes its port and token in a
discovery file and issues a new token, and possibly a new port, every time it
starts. The agent's client contract: read the file and close it right away;
treat a missing file or a refused connection as "not serving"; re-read the file
after a 401.

When the client uses TCP and no `bearer_token` is set, it takes the port and
token from the discovery file, and re-reads the file after a refused connection
or a 401.
"""

from __future__ import annotations

import os
import sys
import json
import threading
from enum import Enum
from typing import Dict, Optional, cast
from dataclasses import dataclass
from typing_extensions import override

import httpx

from .._exceptions import MiruError

__all__ = [
    "AgentTransport",
    "LOOPBACK_HOST",
    "Discovery",
    "DiscoveryError",
    "DiscoveryTransport",
    "AsyncDiscoveryTransport",
    "discovery_for",
    "DiscoveryFile",
    "read_discovery",
    "resolve_transport",
    "default_discovery_file",
]


class AgentTransport(str, Enum):
    """How the client reaches the Miru Agent."""

    UNIX = "unix"
    TCP = "tcp"


# The agent listens on IPv4 loopback only; "localhost" may resolve to ::1 first.
LOOPBACK_HOST = "127.0.0.1"


class DiscoveryError(MiruError):
    """The device API discovery file is missing, unreadable, or invalid."""


@dataclass(frozen=True)
class Discovery:
    port: int
    token: str


class DiscoveryTransport(httpx.BaseTransport):
    """Marks the discovery file stale after a refused connection or a 401.

    The agent may have restarted with a new port or token; the client's retry,
    or its next request when no retry is left, reads the file again.
    """

    def __init__(self, discovery: DiscoveryFile, transport: Optional[httpx.BaseTransport] = None) -> None:
        self._discovery = discovery
        self._transport = transport if transport is not None else httpx.HTTPTransport()

    @override
    def handle_request(self, request: httpx.Request) -> httpx.Response:
        try:
            response = self._transport.handle_request(request)
        except httpx.ConnectError:
            self._discovery.invalidate()
            raise
        if response.status_code == 401:
            self._discovery.invalidate()
        return response

    @override
    def close(self) -> None:
        self._transport.close()


class AsyncDiscoveryTransport(httpx.AsyncBaseTransport):
    """Async counterpart of `DiscoveryTransport`."""

    def __init__(self, discovery: DiscoveryFile, transport: Optional[httpx.AsyncBaseTransport] = None) -> None:
        self._discovery = discovery
        self._transport = transport if transport is not None else httpx.AsyncHTTPTransport()

    @override
    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        try:
            response = await self._transport.handle_async_request(request)
        except httpx.ConnectError:
            self._discovery.invalidate()
            raise
        if response.status_code == 401:
            self._discovery.invalidate()
        return response

    @override
    async def aclose(self) -> None:
        await self._transport.aclose()


_discovery_files: Dict[str, DiscoveryFile] = {}
_discovery_files_lock = threading.Lock()


def discovery_for(
    agent_transport: Optional[str], discovery_file: Optional[str], bearer_token: Optional[str]
) -> Optional[DiscoveryFile]:
    """The discovery file to use, or None when using the Unix socket or an explicit token."""
    if resolve_transport(agent_transport) is not AgentTransport.TCP or bearer_token:
        return None
    path = discovery_file or default_discovery_file()
    with _discovery_files_lock:
        if path not in _discovery_files:
            _discovery_files[path] = DiscoveryFile(path)
        return _discovery_files[path]


class DiscoveryFile:
    """The last read of a discovery file, re-read only after `invalidate()`.

    One instance per path is shared by every client using it (see
    `discovery_for`), so a `copy()` of a client, which keeps the same connection
    pool, also sees the same discovery.
    """

    def __init__(self, path: str) -> None:
        self.path = path
        self._lock = threading.Lock()
        self._current: Optional[Discovery] = None
        self._stale = False

    def token_rotated(self, response: httpx.Response) -> bool:
        """After a 401, re-read the file; True if it now has a different token."""
        self.invalidate()
        try:
            discovery = self.get()
        except DiscoveryError:
            return False
        sent: Optional[str] = response.request.headers.get("Authorization")
        return sent != f"Bearer {discovery.token}"

    def get(self) -> Discovery:
        with self._lock:
            if self._current is None or self._stale:
                try:
                    self._current = read_discovery(self.path)
                    self._stale = False
                except DiscoveryError:
                    if self._current is None:
                        raise
                    # The agent is restarting. Keep the old values: the request
                    # fails to connect, and the client's retry reads again.
            return self._current

    def invalidate(self) -> None:
        with self._lock:
            self._stale = True


def read_discovery(path: str) -> Discovery:
    """Read the port and token (`{"port": ..., "token": ...}`), holding the file
    open only for the read. Other fields are ignored.

    On Windows an open handle stops the agent from replacing or removing the file.
    """
    try:
        with open(path, "rb") as file:
            raw = file.read()
    except FileNotFoundError as err:
        raise DiscoveryError(
            f"Miru Agent discovery file {path} not found: the agent is not running or not serving TCP"
        ) from err
    except PermissionError as err:
        hint = (
            " (run as an administrator or a member of the 'Miru Agent Users' group)" if sys.platform == "win32" else ""
        )
        raise DiscoveryError(f"cannot read Miru Agent discovery file {path}{hint}") from err
    except OSError as err:
        raise DiscoveryError(f"cannot read Miru Agent discovery file {path}: {err}") from err

    try:
        data = json.loads(raw)
    except ValueError as err:
        raise DiscoveryError(f"Miru Agent discovery file {path} is not valid JSON") from err
    if not isinstance(data, dict):
        raise DiscoveryError(f"Miru Agent discovery file {path} is not a JSON object")
    fields = cast(Dict[str, object], data)
    port = fields.get("port")
    if not isinstance(port, int) or isinstance(port, bool) or not 1 <= port <= 65535:
        raise DiscoveryError(f"Miru Agent discovery file {path} has an invalid port")
    token = fields.get("token")
    if not isinstance(token, str) or not token:
        raise DiscoveryError(f"Miru Agent discovery file {path} has an invalid token")
    return Discovery(port=port, token=token)


def resolve_transport(value: Optional[str]) -> AgentTransport:
    """TCP by default on Windows, the Unix socket elsewhere."""
    if value is None or value == "":
        return AgentTransport.TCP if sys.platform == "win32" else AgentTransport.UNIX
    try:
        return AgentTransport(value.strip().lower())
    except ValueError:
        allowed = " or ".join(repr(member.value) for member in AgentTransport)
        raise ValueError(f"agent_transport must be {allowed}, got {value!r}") from None


def default_discovery_file() -> str:
    if sys.platform == "win32":
        program_data = os.environ.get("ProgramData") or "C:\\ProgramData"
        return os.path.join(program_data, "Miru", "device-api", "device-api.json")
    return "/run/miru/device-api.json"
