# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.platform import calibration_list_params, calibration_retrieve_params
from ...types.platform.calibration import Calibration
from ...types.platform.calibration_list import CalibrationList

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

    def retrieve(
        self,
        calibration_id: str,
        *,
        expand: List[Literal["content"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Calibration:
        """
        Retrieve a calibration by its ID from the control plane.

        Args:
          expand: Fields to expand on the calibration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not calibration_id:
            raise ValueError(f"Expected a non-empty value for `calibration_id` but received {calibration_id!r}")
        return self._get(
            path_template("/platform/calibrations/{calibration_id}", calibration_id=calibration_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"expand": expand}, calibration_retrieve_params.CalibrationRetrieveParams),
            ),
            cast_to=Calibration,
        )

    def list(
        self,
        *,
        aspect: SequenceNotStr[str] | Omit = omit,
        component: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["content", "total_count"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[
            Literal["id:asc", "id:desc", "created_at:asc", "created_at:desc", "reported_at:asc", "reported_at:desc"]
        ]
        | Omit = omit,
        report_id: SequenceNotStr[str] | Omit = omit,
        role: SequenceNotStr[str] | Omit = omit,
        serial_number: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalibrationList:
        """
        List the device's calibrations from the control plane.

        Args:
          aspect: The aspect slugs to filter by; `null` matches calibrations reported without an
              aspect. Aspect slugs are unique only within a component, so filter by component
              too to match one component's aspect.

          component: The component slugs to filter by.

          expand: Fields to expand on each calibration in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the calibration results. Ties are broken by `id`.

          report_id: The report IDs to filter by.

          role: The role slugs to filter by; `null` matches calibrations reported without a
              role. Role slugs are unique only within a component, so filter by component too
              to match one component's role.

          serial_number: The unit serial numbers to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/platform/calibrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "aspect": aspect,
                        "component": component,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "report_id": report_id,
                        "role": role,
                        "serial_number": serial_number,
                    },
                    calibration_list_params.CalibrationListParams,
                ),
            ),
            cast_to=CalibrationList,
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

    async def retrieve(
        self,
        calibration_id: str,
        *,
        expand: List[Literal["content"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Calibration:
        """
        Retrieve a calibration by its ID from the control plane.

        Args:
          expand: Fields to expand on the calibration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not calibration_id:
            raise ValueError(f"Expected a non-empty value for `calibration_id` but received {calibration_id!r}")
        return await self._get(
            path_template("/platform/calibrations/{calibration_id}", calibration_id=calibration_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"expand": expand}, calibration_retrieve_params.CalibrationRetrieveParams
                ),
            ),
            cast_to=Calibration,
        )

    async def list(
        self,
        *,
        aspect: SequenceNotStr[str] | Omit = omit,
        component: SequenceNotStr[str] | Omit = omit,
        expand: List[Literal["content", "total_count"]] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        order_by: List[
            Literal["id:asc", "id:desc", "created_at:asc", "created_at:desc", "reported_at:asc", "reported_at:desc"]
        ]
        | Omit = omit,
        report_id: SequenceNotStr[str] | Omit = omit,
        role: SequenceNotStr[str] | Omit = omit,
        serial_number: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CalibrationList:
        """
        List the device's calibrations from the control plane.

        Args:
          aspect: The aspect slugs to filter by; `null` matches calibrations reported without an
              aspect. Aspect slugs are unique only within a component, so filter by component
              too to match one component's aspect.

          component: The component slugs to filter by.

          expand: Fields to expand on each calibration in the list.

          limit: The maximum number of items to return. A limit of 15 with an offset of 0 returns
              items 1-15.

          offset: The offset of the items to return. An offset of 10 with a limit of 10 returns
              items 11-20.

          order_by: Sort order for the calibration results. Ties are broken by `id`.

          report_id: The report IDs to filter by.

          role: The role slugs to filter by; `null` matches calibrations reported without a
              role. Role slugs are unique only within a component, so filter by component too
              to match one component's role.

          serial_number: The unit serial numbers to filter by.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/platform/calibrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "aspect": aspect,
                        "component": component,
                        "expand": expand,
                        "limit": limit,
                        "offset": offset,
                        "order_by": order_by,
                        "report_id": report_id,
                        "role": role,
                        "serial_number": serial_number,
                    },
                    calibration_list_params.CalibrationListParams,
                ),
            ),
            cast_to=CalibrationList,
        )


class CalibrationsResourceWithRawResponse:
    def __init__(self, calibrations: CalibrationsResource) -> None:
        self._calibrations = calibrations

        self.retrieve = to_raw_response_wrapper(
            calibrations.retrieve,
        )
        self.list = to_raw_response_wrapper(
            calibrations.list,
        )


class AsyncCalibrationsResourceWithRawResponse:
    def __init__(self, calibrations: AsyncCalibrationsResource) -> None:
        self._calibrations = calibrations

        self.retrieve = async_to_raw_response_wrapper(
            calibrations.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            calibrations.list,
        )


class CalibrationsResourceWithStreamingResponse:
    def __init__(self, calibrations: CalibrationsResource) -> None:
        self._calibrations = calibrations

        self.retrieve = to_streamed_response_wrapper(
            calibrations.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            calibrations.list,
        )


class AsyncCalibrationsResourceWithStreamingResponse:
    def __init__(self, calibrations: AsyncCalibrationsResource) -> None:
        self._calibrations = calibrations

        self.retrieve = async_to_streamed_response_wrapper(
            calibrations.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            calibrations.list,
        )
