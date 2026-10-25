# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_device_sdk import Miru, AsyncMiru
from miru_device_sdk.types import CalibrationCreateResponse

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
