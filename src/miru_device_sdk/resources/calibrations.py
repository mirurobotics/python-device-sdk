# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import calibration_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.calibration_create_response import CalibrationCreateResponse

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
        component_slug: str,
        content: calibration_create_params.Content,
        aspect: str | Omit = omit,
        role: str | Omit = omit,
        serial_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalibrationCreateResponse:
        """Report a calibration to Miru.

        The agent checks the request, saves the
        calibration on the device and returns right away, without waiting for Miru. It
        uploads saved calibrations to Miru in the order received and retries until Miru
        is reachable, so a calibration survives network outages and agent restarts. The
        agent checks the request against Miru's rules before saving it, so Miru rarely
        rejects one later; one it does reject, such as a new component once the
        workspace holds 100, is set aside on the device and does not hold up later ones.
        Content is at most 1 MiB and a request is at most about 2 MiB (1 MiB of content
        plus JSON escaping). Each request is a new calibration, so sending the same
        calibration twice records it twice. The agent sends the report's `report_id`
        with every upload, so a retried upload does not record the calibration twice.

        Args:
          component_slug: Slug of the component the calibrated unit belongs to. A new slug creates a
              component in Miru.

          content: The calibration's content, at most 1 MiB. The agent uploads it to Miru
              unchanged.

          aspect: Slug of the aspect of the unit that was calibrated, when it has more than one,
              e.g. `intrinsics` vs `extrinsics`, or `pose` vs `home-offsets`. Validated like a
              slug. Miru resolves it to one of the component's `aspects`, creating the aspect
              the first time it is reported.

          role: Slug of the role the calibrated unit fills on the device, such as `aligner-1` or
              `front-left`. Distinguishes several units of one component on a device.
              Validated like a slug. Miru resolves it to one of the component's `roles`,
              creating the role the first time it is reported.

          serial_number: Serial number of the physical unit that was calibrated, not of the device, such
              as `M500-1234`. Free text, at most 255 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/calibrations",
            body=maybe_transform(
                {
                    "component_slug": component_slug,
                    "content": content,
                    "aspect": aspect,
                    "role": role,
                    "serial_number": serial_number,
                },
                calibration_create_params.CalibrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalibrationCreateResponse,
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
        component_slug: str,
        content: calibration_create_params.Content,
        aspect: str | Omit = omit,
        role: str | Omit = omit,
        serial_number: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalibrationCreateResponse:
        """Report a calibration to Miru.

        The agent checks the request, saves the
        calibration on the device and returns right away, without waiting for Miru. It
        uploads saved calibrations to Miru in the order received and retries until Miru
        is reachable, so a calibration survives network outages and agent restarts. The
        agent checks the request against Miru's rules before saving it, so Miru rarely
        rejects one later; one it does reject, such as a new component once the
        workspace holds 100, is set aside on the device and does not hold up later ones.
        Content is at most 1 MiB and a request is at most about 2 MiB (1 MiB of content
        plus JSON escaping). Each request is a new calibration, so sending the same
        calibration twice records it twice. The agent sends the report's `report_id`
        with every upload, so a retried upload does not record the calibration twice.

        Args:
          component_slug: Slug of the component the calibrated unit belongs to. A new slug creates a
              component in Miru.

          content: The calibration's content, at most 1 MiB. The agent uploads it to Miru
              unchanged.

          aspect: Slug of the aspect of the unit that was calibrated, when it has more than one,
              e.g. `intrinsics` vs `extrinsics`, or `pose` vs `home-offsets`. Validated like a
              slug. Miru resolves it to one of the component's `aspects`, creating the aspect
              the first time it is reported.

          role: Slug of the role the calibrated unit fills on the device, such as `aligner-1` or
              `front-left`. Distinguishes several units of one component on a device.
              Validated like a slug. Miru resolves it to one of the component's `roles`,
              creating the role the first time it is reported.

          serial_number: Serial number of the physical unit that was calibrated, not of the device, such
              as `M500-1234`. Free text, at most 255 characters.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/calibrations",
            body=await async_maybe_transform(
                {
                    "component_slug": component_slug,
                    "content": content,
                    "aspect": aspect,
                    "role": role,
                    "serial_number": serial_number,
                },
                calibration_create_params.CalibrationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CalibrationCreateResponse,
        )


class CalibrationsResourceWithRawResponse:
    def __init__(self, calibrations: CalibrationsResource) -> None:
        self._calibrations = calibrations

        self.create = to_raw_response_wrapper(
            calibrations.create,
        )


class AsyncCalibrationsResourceWithRawResponse:
    def __init__(self, calibrations: AsyncCalibrationsResource) -> None:
        self._calibrations = calibrations

        self.create = async_to_raw_response_wrapper(
            calibrations.create,
        )


class CalibrationsResourceWithStreamingResponse:
    def __init__(self, calibrations: CalibrationsResource) -> None:
        self._calibrations = calibrations

        self.create = to_streamed_response_wrapper(
            calibrations.create,
        )


class AsyncCalibrationsResourceWithStreamingResponse:
    def __init__(self, calibrations: AsyncCalibrationsResource) -> None:
        self._calibrations = calibrations

        self.create = async_to_streamed_response_wrapper(
            calibrations.create,
        )
