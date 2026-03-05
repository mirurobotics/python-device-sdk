# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.git_commit_retrieve_response import GitCommitRetrieveResponse

__all__ = ["GitCommitsResource", "AsyncGitCommitsResource"]


class GitCommitsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GitCommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/miru-device-python#accessing-raw-response-data-eg-headers
        """
        return GitCommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitCommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/miru-device-python#with_streaming_response
        """
        return GitCommitsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        git_commit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitCommitRetrieveResponse:
        """
        Retrieve a git commit by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not git_commit_id:
            raise ValueError(f"Expected a non-empty value for `git_commit_id` but received {git_commit_id!r}")
        return self._get(
            f"/git_commits/{git_commit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitCommitRetrieveResponse,
        )


class AsyncGitCommitsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGitCommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/miru-device-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGitCommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitCommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/miru-device-python#with_streaming_response
        """
        return AsyncGitCommitsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        git_commit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GitCommitRetrieveResponse:
        """
        Retrieve a git commit by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not git_commit_id:
            raise ValueError(f"Expected a non-empty value for `git_commit_id` but received {git_commit_id!r}")
        return await self._get(
            f"/git_commits/{git_commit_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GitCommitRetrieveResponse,
        )


class GitCommitsResourceWithRawResponse:
    def __init__(self, git_commits: GitCommitsResource) -> None:
        self._git_commits = git_commits

        self.retrieve = to_raw_response_wrapper(
            git_commits.retrieve,
        )


class AsyncGitCommitsResourceWithRawResponse:
    def __init__(self, git_commits: AsyncGitCommitsResource) -> None:
        self._git_commits = git_commits

        self.retrieve = async_to_raw_response_wrapper(
            git_commits.retrieve,
        )


class GitCommitsResourceWithStreamingResponse:
    def __init__(self, git_commits: GitCommitsResource) -> None:
        self._git_commits = git_commits

        self.retrieve = to_streamed_response_wrapper(
            git_commits.retrieve,
        )


class AsyncGitCommitsResourceWithStreamingResponse:
    def __init__(self, git_commits: AsyncGitCommitsResource) -> None:
        self._git_commits = git_commits

        self.retrieve = async_to_streamed_response_wrapper(
            git_commits.retrieve,
        )
