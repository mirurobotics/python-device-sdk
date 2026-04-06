# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import event_stream_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, strip_not_given, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._streaming import Stream, AsyncStream
from ..types.event import Event
from .._base_client import make_request_options

__all__ = ["EventsResource", "AsyncEventsResource"]


class EventsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#accessing-raw-response-data-eg-headers
        """
        return EventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#with_streaming_response
        """
        return EventsResourceWithStreamingResponse(self)

    def stream(
        self,
        *,
        after: int | Omit = omit,
        types: SequenceNotStr[str] | Omit = omit,
        last_event_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[Event]:
        """
        Subscribe to a Server-Sent Events (SSE) stream of agent lifecycle events.

        The stream replays retained historical events after the cursor, then delivers
        live events as they occur. Events are delivered at-least-once; clients should
        deduplicate by event `id`.

        Use the `after` query parameter or `Last-Event-ID` header to resume from a
        previous position. If the cursor is older than the earliest retained event, the
        server returns `410 Gone`.

        Args:
          after: Event ID cursor. Only events with `id` greater than this value are returned.
              Takes precedence over the `Last-Event-ID` header.

          types: Event types to receive. If omitted, all event types are sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Last-Event-ID": last_event_id}), **(extra_headers or {})}
        return self._get(
            "/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "types": types,
                    },
                    event_stream_params.EventStreamParams,
                ),
            ),
            cast_to=Event,
            stream=True,
            stream_cls=Stream[Event],
        )


class AsyncEventsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEventsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncEventsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEventsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#with_streaming_response
        """
        return AsyncEventsResourceWithStreamingResponse(self)

    async def stream(
        self,
        *,
        after: int | Omit = omit,
        types: SequenceNotStr[str] | Omit = omit,
        last_event_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[Event]:
        """
        Subscribe to a Server-Sent Events (SSE) stream of agent lifecycle events.

        The stream replays retained historical events after the cursor, then delivers
        live events as they occur. Events are delivered at-least-once; clients should
        deduplicate by event `id`.

        Use the `after` query parameter or `Last-Event-ID` header to resume from a
        previous position. If the cursor is older than the earliest retained event, the
        server returns `410 Gone`.

        Args:
          after: Event ID cursor. Only events with `id` greater than this value are returned.
              Takes precedence over the `Last-Event-ID` header.

          types: Event types to receive. If omitted, all event types are sent.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"Last-Event-ID": last_event_id}), **(extra_headers or {})}
        return await self._get(
            "/events",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "types": types,
                    },
                    event_stream_params.EventStreamParams,
                ),
            ),
            cast_to=Event,
            stream=True,
            stream_cls=AsyncStream[Event],
        )


class EventsResourceWithRawResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.stream = to_raw_response_wrapper(
            events.stream,
        )


class AsyncEventsResourceWithRawResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.stream = async_to_raw_response_wrapper(
            events.stream,
        )


class EventsResourceWithStreamingResponse:
    def __init__(self, events: EventsResource) -> None:
        self._events = events

        self.stream = to_streamed_response_wrapper(
            events.stream,
        )


class AsyncEventsResourceWithStreamingResponse:
    def __init__(self, events: AsyncEventsResource) -> None:
        self._events = events

        self.stream = async_to_streamed_response_wrapper(
            events.stream,
        )
