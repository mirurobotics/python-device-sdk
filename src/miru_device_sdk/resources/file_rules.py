# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import path_template
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.file_rule import FileRule

__all__ = ["FileRulesResource", "AsyncFileRulesResource"]


class FileRulesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FileRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#accessing-raw-response-data-eg-headers
        """
        return FileRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FileRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#with_streaming_response
        """
        return FileRulesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        file_rule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRule:
        """
        Retrieve a file rule by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_rule_id:
            raise ValueError(f"Expected a non-empty value for `file_rule_id` but received {file_rule_id!r}")
        return self._get(
            path_template("/file_rules/{file_rule_id}", file_rule_id=file_rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRule,
        )


class AsyncFileRulesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFileRulesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncFileRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFileRulesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#with_streaming_response
        """
        return AsyncFileRulesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        file_rule_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRule:
        """
        Retrieve a file rule by its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_rule_id:
            raise ValueError(f"Expected a non-empty value for `file_rule_id` but received {file_rule_id!r}")
        return await self._get(
            path_template("/file_rules/{file_rule_id}", file_rule_id=file_rule_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRule,
        )


class FileRulesResourceWithRawResponse:
    def __init__(self, file_rules: FileRulesResource) -> None:
        self._file_rules = file_rules

        self.retrieve = to_raw_response_wrapper(
            file_rules.retrieve,
        )


class AsyncFileRulesResourceWithRawResponse:
    def __init__(self, file_rules: AsyncFileRulesResource) -> None:
        self._file_rules = file_rules

        self.retrieve = async_to_raw_response_wrapper(
            file_rules.retrieve,
        )


class FileRulesResourceWithStreamingResponse:
    def __init__(self, file_rules: FileRulesResource) -> None:
        self._file_rules = file_rules

        self.retrieve = to_streamed_response_wrapper(
            file_rules.retrieve,
        )


class AsyncFileRulesResourceWithStreamingResponse:
    def __init__(self, file_rules: AsyncFileRulesResource) -> None:
        self._file_rules = file_rules

        self.retrieve = async_to_streamed_response_wrapper(
            file_rules.retrieve,
        )
