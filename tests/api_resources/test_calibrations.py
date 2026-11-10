# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from miru_device_sdk import Miru, AsyncMiru
from miru_device_sdk.types import (
    CalibrationCreateResponse,
    CalibrationLatestResponse,
)
from miru_device_sdk._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalibrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Miru) -> None:
        calibration = client.calibrations.create(
            component="arm",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
        )
        assert_matches_type(CalibrationCreateResponse, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Miru) -> None:
        calibration = client.calibrations.create(
            component="arm",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
            aspect="pose",
            reported_by="Benjamin Smidt",
            role="front-left",
            serial_number="SN-1234",
        )
        assert_matches_type(CalibrationCreateResponse, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Miru) -> None:
        response = client.calibrations.with_raw_response.create(
            component="arm",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = response.parse()
        assert_matches_type(CalibrationCreateResponse, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Miru) -> None:
        with client.calibrations.with_streaming_response.create(
            component="arm",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = response.parse()
            assert_matches_type(CalibrationCreateResponse, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Miru, respx_mock: MockRouter) -> None:
        respx_mock.get("/calibrations/latest/0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        calibration = client.calibrations.download(
            "0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10",
        )
        assert calibration.is_closed
        assert calibration.json() == {"foo": "bar"}
        assert cast(Any, calibration.is_closed) is True
        assert isinstance(calibration, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Miru, respx_mock: MockRouter) -> None:
        respx_mock.get("/calibrations/latest/0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        calibration = client.calibrations.with_raw_response.download(
            "0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10",
        )

        assert calibration.is_closed is True
        assert calibration.http_request.headers.get("X-Stainless-Lang") == "python"
        assert calibration.json() == {"foo": "bar"}
        assert isinstance(calibration, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Miru, respx_mock: MockRouter) -> None:
        respx_mock.get("/calibrations/latest/0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.calibrations.with_streaming_response.download(
            "0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10",
        ) as calibration:
            assert not calibration.is_closed
            assert calibration.http_request.headers.get("X-Stainless-Lang") == "python"

            assert calibration.json() == {"foo": "bar"}
            assert cast(Any, calibration.is_closed) is True
            assert isinstance(calibration, StreamedBinaryAPIResponse)

        assert cast(Any, calibration.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            client.calibrations.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_latest(self, client: Miru) -> None:
        calibration = client.calibrations.latest()
        assert_matches_type(CalibrationLatestResponse, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_latest_with_all_params(self, client: Miru) -> None:
        calibration = client.calibrations.latest(
            aspect=["pose"],
            component=["arm"],
            role=["front-left"],
        )
        assert_matches_type(CalibrationLatestResponse, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_latest(self, client: Miru) -> None:
        response = client.calibrations.with_raw_response.latest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = response.parse()
        assert_matches_type(CalibrationLatestResponse, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_latest(self, client: Miru) -> None:
        with client.calibrations.with_streaming_response.latest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = response.parse()
            assert_matches_type(CalibrationLatestResponse, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCalibrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMiru) -> None:
        calibration = await async_client.calibrations.create(
            component="arm",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
        )
        assert_matches_type(CalibrationCreateResponse, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMiru) -> None:
        calibration = await async_client.calibrations.create(
            component="arm",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
            aspect="pose",
            reported_by="Benjamin Smidt",
            role="front-left",
            serial_number="SN-1234",
        )
        assert_matches_type(CalibrationCreateResponse, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMiru) -> None:
        response = await async_client.calibrations.with_raw_response.create(
            component="arm",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = await response.parse()
        assert_matches_type(CalibrationCreateResponse, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMiru) -> None:
        async with async_client.calibrations.with_streaming_response.create(
            component="arm",
            content={
                "data": '{\n  "enable_autonomy": true,\n  "enable_remote_control": true,\n  "max_payload_kg": 10.0\n}\n',
                "format": "json",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = await response.parse()
            assert_matches_type(CalibrationCreateResponse, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncMiru, respx_mock: MockRouter) -> None:
        respx_mock.get("/calibrations/latest/0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        calibration = await async_client.calibrations.download(
            "0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10",
        )
        assert calibration.is_closed
        assert await calibration.json() == {"foo": "bar"}
        assert cast(Any, calibration.is_closed) is True
        assert isinstance(calibration, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncMiru, respx_mock: MockRouter) -> None:
        respx_mock.get("/calibrations/latest/0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        calibration = await async_client.calibrations.with_raw_response.download(
            "0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10",
        )

        assert calibration.is_closed is True
        assert calibration.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await calibration.json() == {"foo": "bar"}
        assert isinstance(calibration, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncMiru, respx_mock: MockRouter) -> None:
        respx_mock.get("/calibrations/latest/0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10/content").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.calibrations.with_streaming_response.download(
            "0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10",
        ) as calibration:
            assert not calibration.is_closed
            assert calibration.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await calibration.json() == {"foo": "bar"}
            assert cast(Any, calibration.is_closed) is True
            assert isinstance(calibration, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, calibration.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `report_id` but received ''"):
            await async_client.calibrations.with_raw_response.download(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_latest(self, async_client: AsyncMiru) -> None:
        calibration = await async_client.calibrations.latest()
        assert_matches_type(CalibrationLatestResponse, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_latest_with_all_params(self, async_client: AsyncMiru) -> None:
        calibration = await async_client.calibrations.latest(
            aspect=["pose"],
            component=["arm"],
            role=["front-left"],
        )
        assert_matches_type(CalibrationLatestResponse, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_latest(self, async_client: AsyncMiru) -> None:
        response = await async_client.calibrations.with_raw_response.latest()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = await response.parse()
        assert_matches_type(CalibrationLatestResponse, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_latest(self, async_client: AsyncMiru) -> None:
        async with async_client.calibrations.with_streaming_response.latest() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = await response.parse()
            assert_matches_type(CalibrationLatestResponse, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True
