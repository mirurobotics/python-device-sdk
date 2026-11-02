# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .calibrations import (
    CalibrationsResource,
    AsyncCalibrationsResource,
    CalibrationsResourceWithRawResponse,
    AsyncCalibrationsResourceWithRawResponse,
    CalibrationsResourceWithStreamingResponse,
    AsyncCalibrationsResourceWithStreamingResponse,
)

__all__ = ["PlatformResource", "AsyncPlatformResource"]


class PlatformResource(SyncAPIResource):
    @cached_property
    def calibrations(self) -> CalibrationsResource:
        return CalibrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PlatformResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#accessing-raw-response-data-eg-headers
        """
        return PlatformResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PlatformResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#with_streaming_response
        """
        return PlatformResourceWithStreamingResponse(self)


class AsyncPlatformResource(AsyncAPIResource):
    @cached_property
    def calibrations(self) -> AsyncCalibrationsResource:
        return AsyncCalibrationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPlatformResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncPlatformResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPlatformResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/mirurobotics/python-device-sdk#with_streaming_response
        """
        return AsyncPlatformResourceWithStreamingResponse(self)


class PlatformResourceWithRawResponse:
    def __init__(self, platform: PlatformResource) -> None:
        self._platform = platform

    @cached_property
    def calibrations(self) -> CalibrationsResourceWithRawResponse:
        return CalibrationsResourceWithRawResponse(self._platform.calibrations)


class AsyncPlatformResourceWithRawResponse:
    def __init__(self, platform: AsyncPlatformResource) -> None:
        self._platform = platform

    @cached_property
    def calibrations(self) -> AsyncCalibrationsResourceWithRawResponse:
        return AsyncCalibrationsResourceWithRawResponse(self._platform.calibrations)


class PlatformResourceWithStreamingResponse:
    def __init__(self, platform: PlatformResource) -> None:
        self._platform = platform

    @cached_property
    def calibrations(self) -> CalibrationsResourceWithStreamingResponse:
        return CalibrationsResourceWithStreamingResponse(self._platform.calibrations)


class AsyncPlatformResourceWithStreamingResponse:
    def __init__(self, platform: AsyncPlatformResource) -> None:
        self._platform = platform

    @cached_property
    def calibrations(self) -> AsyncCalibrationsResourceWithStreamingResponse:
        return AsyncCalibrationsResourceWithStreamingResponse(self._platform.calibrations)
