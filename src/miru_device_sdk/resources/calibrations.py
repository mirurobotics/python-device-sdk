# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import calibration_create_params, calibration_latest_params, calibration_invalidate_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.calibration import Calibration
from ..types.calibration_create_response import CalibrationCreateResponse
from ..types.calibration_latest_response import CalibrationLatestResponse

__all__ = ["CalibrationsResource", "AsyncCalibrationsResource"]


class CalibrationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CalibrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#accessing-raw-response-data-eg-headers
        """
        return CalibrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalibrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#with_streaming_response
        """
        return CalibrationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        component: str,
        content: calibration_create_params.Content,
        reported_by: str | Omit = omit,
        serial_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalibrationCreateResponse:
        """
        Report a calibration to Miru.

        Args:
          component: Slug of the component the calibrated unit belongs to, such as `arm`. Miru
              resolves it to the component, creating the component the first time it is
              reported.

          content: The calibration's content, at most 1 MiB. The agent uploads it to Miru
              unchanged.

          reported_by: Who reported the calibration, as the device knows them, such as
              `Benjamin Smidt`. Free text, at most 255 characters. Miru stores it unchanged.

          serial_number: Serial number of the physical unit that was calibrated, not of the device, such
              as `SN-1234`. Free text, at most 255 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/calibrations",
            body=maybe_transform(
                {
                    "component": component,
                    "content": content,
                    "reported_by": reported_by,
                    "serial_number": serial_number,
                },
                calibration_create_params.CalibrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalibrationCreateResponse,
        )

    def download(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Download the content of a latest calibration by its report ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            path_template("/calibrations/latest/{report_id}/content", report_id=report_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def invalidate(
        self,
        *,
        component: str,
        reason: str,
        report_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Calibration:
        """
        Mark a component's latest calibration invalid.

        Args:
          component: Slug of the component whose latest calibration to invalidate, such as `arm`.

          reason: Why the calibration is no longer valid, such as `power cycle`. Free text, at
              most 512 characters, and not blank.

          report_id: Report ID of the calibration the caller expects to be `component`'s latest. If
              it is not `component`'s current latest calibration, the agent invalidates
              nothing. Leave it out to invalidate whatever is latest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/calibrations/latest/invalidate",
            body=maybe_transform(
                {
                    "component": component,
                    "reason": reason,
                    "report_id": report_id,
                },
                calibration_invalidate_params.CalibrationInvalidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Calibration,
        )

    def latest(
        self,
        *,
        component: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalibrationLatestResponse:
        """
        List the latest calibration for each component on the device.

        Args:
          component: The component slugs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/calibrations/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"component": component}, calibration_latest_params.CalibrationLatestParams),
            ),
            cast_to=CalibrationLatestResponse,
        )


class AsyncCalibrationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCalibrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCalibrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalibrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#with_streaming_response
        """
        return AsyncCalibrationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        component: str,
        content: calibration_create_params.Content,
        reported_by: str | Omit = omit,
        serial_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalibrationCreateResponse:
        """
        Report a calibration to Miru.

        Args:
          component: Slug of the component the calibrated unit belongs to, such as `arm`. Miru
              resolves it to the component, creating the component the first time it is
              reported.

          content: The calibration's content, at most 1 MiB. The agent uploads it to Miru
              unchanged.

          reported_by: Who reported the calibration, as the device knows them, such as
              `Benjamin Smidt`. Free text, at most 255 characters. Miru stores it unchanged.

          serial_number: Serial number of the physical unit that was calibrated, not of the device, such
              as `SN-1234`. Free text, at most 255 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/calibrations",
            body=await async_maybe_transform(
                {
                    "component": component,
                    "content": content,
                    "reported_by": reported_by,
                    "serial_number": serial_number,
                },
                calibration_create_params.CalibrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalibrationCreateResponse,
        )

    async def download(
        self,
        report_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Download the content of a latest calibration by its report ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not report_id:
            raise ValueError(f"Expected a non-empty value for `report_id` but received {report_id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            path_template("/calibrations/latest/{report_id}/content", report_id=report_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def invalidate(
        self,
        *,
        component: str,
        reason: str,
        report_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Calibration:
        """
        Mark a component's latest calibration invalid.

        Args:
          component: Slug of the component whose latest calibration to invalidate, such as `arm`.

          reason: Why the calibration is no longer valid, such as `power cycle`. Free text, at
              most 512 characters, and not blank.

          report_id: Report ID of the calibration the caller expects to be `component`'s latest. If
              it is not `component`'s current latest calibration, the agent invalidates
              nothing. Leave it out to invalidate whatever is latest.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/calibrations/latest/invalidate",
            body=await async_maybe_transform(
                {
                    "component": component,
                    "reason": reason,
                    "report_id": report_id,
                },
                calibration_invalidate_params.CalibrationInvalidateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Calibration,
        )

    async def latest(
        self,
        *,
        component: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalibrationLatestResponse:
        """
        List the latest calibration for each component on the device.

        Args:
          component: The component slugs to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/calibrations/latest",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"component": component}, calibration_latest_params.CalibrationLatestParams
                ),
            ),
            cast_to=CalibrationLatestResponse,
        )


class CalibrationsResourceWithRawResponse:
    def __init__(self, calibrations: CalibrationsResource) -> None:
        self._calibrations = calibrations

        self.create = to_raw_response_wrapper(
            calibrations.create,
        )
        self.download = to_custom_raw_response_wrapper(
            calibrations.download,
            BinaryAPIResponse,
        )
        self.invalidate = to_raw_response_wrapper(
            calibrations.invalidate,
        )
        self.latest = to_raw_response_wrapper(
            calibrations.latest,
        )


class AsyncCalibrationsResourceWithRawResponse:
    def __init__(self, calibrations: AsyncCalibrationsResource) -> None:
        self._calibrations = calibrations

        self.create = async_to_raw_response_wrapper(
            calibrations.create,
        )
        self.download = async_to_custom_raw_response_wrapper(
            calibrations.download,
            AsyncBinaryAPIResponse,
        )
        self.invalidate = async_to_raw_response_wrapper(
            calibrations.invalidate,
        )
        self.latest = async_to_raw_response_wrapper(
            calibrations.latest,
        )


class CalibrationsResourceWithStreamingResponse:
    def __init__(self, calibrations: CalibrationsResource) -> None:
        self._calibrations = calibrations

        self.create = to_streamed_response_wrapper(
            calibrations.create,
        )
        self.download = to_custom_streamed_response_wrapper(
            calibrations.download,
            StreamedBinaryAPIResponse,
        )
        self.invalidate = to_streamed_response_wrapper(
            calibrations.invalidate,
        )
        self.latest = to_streamed_response_wrapper(
            calibrations.latest,
        )


class AsyncCalibrationsResourceWithStreamingResponse:
    def __init__(self, calibrations: AsyncCalibrationsResource) -> None:
        self._calibrations = calibrations

        self.create = async_to_streamed_response_wrapper(
            calibrations.create,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            calibrations.download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.invalidate = async_to_streamed_response_wrapper(
            calibrations.invalidate,
        )
        self.latest = async_to_streamed_response_wrapper(
            calibrations.latest,
        )
