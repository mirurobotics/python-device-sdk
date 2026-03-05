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
from ..types.release import Release

__all__ = ["ReleasesResource", "AsyncReleasesResource"]


class ReleasesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReleasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/miru-device-python#accessing-raw-response-data-eg-headers
        """
        return ReleasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReleasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/miru-device-python#with_streaming_response
        """
        return ReleasesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        release_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Release:
        """
        Retrieve a release by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not release_id:
            raise ValueError(f"Expected a non-empty value for `release_id` but received {release_id!r}")
        return self._get(
            f"/releases/{release_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Release,
        )

    def retrieve_current(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Release:
        """Retrieve the current release."""
        return self._get(
            "/releases/current",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Release,
        )


class AsyncReleasesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReleasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/miru-device-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReleasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReleasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/miru-device-python#with_streaming_response
        """
        return AsyncReleasesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        release_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Release:
        """
        Retrieve a release by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not release_id:
            raise ValueError(f"Expected a non-empty value for `release_id` but received {release_id!r}")
        return await self._get(
            f"/releases/{release_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Release,
        )

    async def retrieve_current(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Release:
        """Retrieve the current release."""
        return await self._get(
            "/releases/current",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Release,
        )


class ReleasesResourceWithRawResponse:
    def __init__(self, releases: ReleasesResource) -> None:
        self._releases = releases

        self.retrieve = to_raw_response_wrapper(
            releases.retrieve,
        )
        self.retrieve_current = to_raw_response_wrapper(
            releases.retrieve_current,
        )


class AsyncReleasesResourceWithRawResponse:
    def __init__(self, releases: AsyncReleasesResource) -> None:
        self._releases = releases

        self.retrieve = async_to_raw_response_wrapper(
            releases.retrieve,
        )
        self.retrieve_current = async_to_raw_response_wrapper(
            releases.retrieve_current,
        )


class ReleasesResourceWithStreamingResponse:
    def __init__(self, releases: ReleasesResource) -> None:
        self._releases = releases

        self.retrieve = to_streamed_response_wrapper(
            releases.retrieve,
        )
        self.retrieve_current = to_streamed_response_wrapper(
            releases.retrieve_current,
        )


class AsyncReleasesResourceWithStreamingResponse:
    def __init__(self, releases: AsyncReleasesResource) -> None:
        self._releases = releases

        self.retrieve = async_to_streamed_response_wrapper(
            releases.retrieve,
        )
        self.retrieve_current = async_to_streamed_response_wrapper(
            releases.retrieve_current,
        )
