# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping, cast
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError
from ._base_client import (
    DEFAULT_TIMEOUT,
    DEFAULT_MAX_RETRIES,
    DEFAULT_CONNECTION_LIMITS,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import agent, device, releases, deployments, git_commits
    from .resources.agent import AgentResource, AsyncAgentResource
    from .resources.device import DeviceResource, AsyncDeviceResource
    from .resources.releases import ReleasesResource, AsyncReleasesResource
    from .resources.deployments import DeploymentsResource, AsyncDeploymentsResource
    from .resources.git_commits import GitCommitsResource, AsyncGitCommitsResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Miru", "AsyncMiru", "Client", "AsyncClient"]


def _build_sync_httpx_client(
    *,
    socket_path: str,
    base_url: str | httpx.URL,
    timeout: float | Timeout | None | NotGiven,
) -> httpx.Client:
    return httpx.Client(
        base_url=base_url,
        timeout=cast(Timeout, timeout if is_given(timeout) else DEFAULT_TIMEOUT),
        limits=DEFAULT_CONNECTION_LIMITS,
        follow_redirects=True,
        transport=httpx.HTTPTransport(uds=socket_path),
    )


def _build_async_httpx_client(
    *,
    socket_path: str,
    base_url: str | httpx.URL,
    timeout: float | Timeout | None | NotGiven,
) -> httpx.AsyncClient:
    return httpx.AsyncClient(
        base_url=base_url,
        timeout=cast(Timeout, timeout if is_given(timeout) else DEFAULT_TIMEOUT),
        limits=DEFAULT_CONNECTION_LIMITS,
        follow_redirects=True,
        transport=httpx.AsyncHTTPTransport(uds=socket_path),
    )


class Miru(SyncAPIClient):
    # client options
    socket_path: str

    def __init__(
        self,
        *,
        socket_path: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Miru client instance.

        This automatically infers the `socket_path` argument from the `MIRU_AGENT_SOCKET` environment variable if it is not provided.
        """
        if socket_path is None:
            socket_path = os.environ.get("MIRU_AGENT_SOCKET") or "/run/miru/miru.sock"
        self.socket_path = socket_path

        if base_url is None:
            base_url = os.environ.get("MIRU_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost/v0.2"
        if http_client is None:
            http_client = _build_sync_httpx_client(
                socket_path=socket_path,
                base_url=base_url,
                timeout=timeout,
            )

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def agent(self) -> AgentResource:
        from .resources.agent import AgentResource

        return AgentResource(self)

    @cached_property
    def deployments(self) -> DeploymentsResource:
        from .resources.deployments import DeploymentsResource

        return DeploymentsResource(self)

    @cached_property
    def device(self) -> DeviceResource:
        from .resources.device import DeviceResource

        return DeviceResource(self)

    @cached_property
    def git_commits(self) -> GitCommitsResource:
        from .resources.git_commits import GitCommitsResource

        return GitCommitsResource(self)

    @cached_property
    def releases(self) -> ReleasesResource:
        from .resources.releases import ReleasesResource

        return ReleasesResource(self)

    @cached_property
    def with_raw_response(self) -> MiruWithRawResponse:
        return MiruWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MiruWithStreamedResponse:
        return MiruWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        socket_path: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            socket_path=socket_path or self.socket_path,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMiru(AsyncAPIClient):
    # client options
    socket_path: str

    def __init__(
        self,
        *,
        socket_path: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncMiru client instance.

        This automatically infers the `socket_path` argument from the `MIRU_AGENT_SOCKET` environment variable if it is not provided.
        """
        if socket_path is None:
            socket_path = os.environ.get("MIRU_AGENT_SOCKET") or "/run/miru/miru.sock"
        self.socket_path = socket_path

        if base_url is None:
            base_url = os.environ.get("MIRU_BASE_URL")
        if base_url is None:
            base_url = f"http://localhost/v0.2"
        if http_client is None:
            http_client = _build_async_httpx_client(
                socket_path=socket_path,
                base_url=base_url,
                timeout=timeout,
            )

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def agent(self) -> AsyncAgentResource:
        from .resources.agent import AsyncAgentResource

        return AsyncAgentResource(self)

    @cached_property
    def deployments(self) -> AsyncDeploymentsResource:
        from .resources.deployments import AsyncDeploymentsResource

        return AsyncDeploymentsResource(self)

    @cached_property
    def device(self) -> AsyncDeviceResource:
        from .resources.device import AsyncDeviceResource

        return AsyncDeviceResource(self)

    @cached_property
    def git_commits(self) -> AsyncGitCommitsResource:
        from .resources.git_commits import AsyncGitCommitsResource

        return AsyncGitCommitsResource(self)

    @cached_property
    def releases(self) -> AsyncReleasesResource:
        from .resources.releases import AsyncReleasesResource

        return AsyncReleasesResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncMiruWithRawResponse:
        return AsyncMiruWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMiruWithStreamedResponse:
        return AsyncMiruWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        socket_path: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            socket_path=socket_path or self.socket_path,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MiruWithRawResponse:
    _client: Miru

    def __init__(self, client: Miru) -> None:
        self._client = client

    @cached_property
    def agent(self) -> agent.AgentResourceWithRawResponse:
        from .resources.agent import AgentResourceWithRawResponse

        return AgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def deployments(self) -> deployments.DeploymentsResourceWithRawResponse:
        from .resources.deployments import DeploymentsResourceWithRawResponse

        return DeploymentsResourceWithRawResponse(self._client.deployments)

    @cached_property
    def device(self) -> device.DeviceResourceWithRawResponse:
        from .resources.device import DeviceResourceWithRawResponse

        return DeviceResourceWithRawResponse(self._client.device)

    @cached_property
    def git_commits(self) -> git_commits.GitCommitsResourceWithRawResponse:
        from .resources.git_commits import GitCommitsResourceWithRawResponse

        return GitCommitsResourceWithRawResponse(self._client.git_commits)

    @cached_property
    def releases(self) -> releases.ReleasesResourceWithRawResponse:
        from .resources.releases import ReleasesResourceWithRawResponse

        return ReleasesResourceWithRawResponse(self._client.releases)


class AsyncMiruWithRawResponse:
    _client: AsyncMiru

    def __init__(self, client: AsyncMiru) -> None:
        self._client = client

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithRawResponse:
        from .resources.agent import AsyncAgentResourceWithRawResponse

        return AsyncAgentResourceWithRawResponse(self._client.agent)

    @cached_property
    def deployments(self) -> deployments.AsyncDeploymentsResourceWithRawResponse:
        from .resources.deployments import AsyncDeploymentsResourceWithRawResponse

        return AsyncDeploymentsResourceWithRawResponse(self._client.deployments)

    @cached_property
    def device(self) -> device.AsyncDeviceResourceWithRawResponse:
        from .resources.device import AsyncDeviceResourceWithRawResponse

        return AsyncDeviceResourceWithRawResponse(self._client.device)

    @cached_property
    def git_commits(self) -> git_commits.AsyncGitCommitsResourceWithRawResponse:
        from .resources.git_commits import AsyncGitCommitsResourceWithRawResponse

        return AsyncGitCommitsResourceWithRawResponse(self._client.git_commits)

    @cached_property
    def releases(self) -> releases.AsyncReleasesResourceWithRawResponse:
        from .resources.releases import AsyncReleasesResourceWithRawResponse

        return AsyncReleasesResourceWithRawResponse(self._client.releases)


class MiruWithStreamedResponse:
    _client: Miru

    def __init__(self, client: Miru) -> None:
        self._client = client

    @cached_property
    def agent(self) -> agent.AgentResourceWithStreamingResponse:
        from .resources.agent import AgentResourceWithStreamingResponse

        return AgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def deployments(self) -> deployments.DeploymentsResourceWithStreamingResponse:
        from .resources.deployments import DeploymentsResourceWithStreamingResponse

        return DeploymentsResourceWithStreamingResponse(self._client.deployments)

    @cached_property
    def device(self) -> device.DeviceResourceWithStreamingResponse:
        from .resources.device import DeviceResourceWithStreamingResponse

        return DeviceResourceWithStreamingResponse(self._client.device)

    @cached_property
    def git_commits(self) -> git_commits.GitCommitsResourceWithStreamingResponse:
        from .resources.git_commits import GitCommitsResourceWithStreamingResponse

        return GitCommitsResourceWithStreamingResponse(self._client.git_commits)

    @cached_property
    def releases(self) -> releases.ReleasesResourceWithStreamingResponse:
        from .resources.releases import ReleasesResourceWithStreamingResponse

        return ReleasesResourceWithStreamingResponse(self._client.releases)


class AsyncMiruWithStreamedResponse:
    _client: AsyncMiru

    def __init__(self, client: AsyncMiru) -> None:
        self._client = client

    @cached_property
    def agent(self) -> agent.AsyncAgentResourceWithStreamingResponse:
        from .resources.agent import AsyncAgentResourceWithStreamingResponse

        return AsyncAgentResourceWithStreamingResponse(self._client.agent)

    @cached_property
    def deployments(self) -> deployments.AsyncDeploymentsResourceWithStreamingResponse:
        from .resources.deployments import AsyncDeploymentsResourceWithStreamingResponse

        return AsyncDeploymentsResourceWithStreamingResponse(self._client.deployments)

    @cached_property
    def device(self) -> device.AsyncDeviceResourceWithStreamingResponse:
        from .resources.device import AsyncDeviceResourceWithStreamingResponse

        return AsyncDeviceResourceWithStreamingResponse(self._client.device)

    @cached_property
    def git_commits(self) -> git_commits.AsyncGitCommitsResourceWithStreamingResponse:
        from .resources.git_commits import AsyncGitCommitsResourceWithStreamingResponse

        return AsyncGitCommitsResourceWithStreamingResponse(self._client.git_commits)

    @cached_property
    def releases(self) -> releases.AsyncReleasesResourceWithStreamingResponse:
        from .resources.releases import AsyncReleasesResourceWithStreamingResponse

        return AsyncReleasesResourceWithStreamingResponse(self._client.releases)


Client = Miru

AsyncClient = AsyncMiru
