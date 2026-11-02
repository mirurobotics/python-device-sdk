# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from miru_device_sdk import Miru, AsyncMiru
from miru_device_sdk.types.platform import (
    Calibration,
    CalibrationList,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCalibrations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Miru) -> None:
        calibration = client.platform.calibrations.retrieve(
            calibration_id="cal_123",
        )
        assert_matches_type(Calibration, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Miru) -> None:
        calibration = client.platform.calibrations.retrieve(
            calibration_id="cal_123",
            expand=["content"],
        )
        assert_matches_type(Calibration, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Miru) -> None:
        response = client.platform.calibrations.with_raw_response.retrieve(
            calibration_id="cal_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = response.parse()
        assert_matches_type(Calibration, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Miru) -> None:
        with client.platform.calibrations.with_streaming_response.retrieve(
            calibration_id="cal_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = response.parse()
            assert_matches_type(Calibration, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Miru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `calibration_id` but received ''"):
            client.platform.calibrations.with_raw_response.retrieve(
                calibration_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Miru) -> None:
        calibration = client.platform.calibrations.list()
        assert_matches_type(CalibrationList, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Miru) -> None:
        calibration = client.platform.calibrations.list(
            aspect=["pose"],
            component=["arm"],
            expand=["content"],
            limit=10,
            offset=0,
            order_by=["created_at:desc"],
            report_id=["0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10"],
            role=["front-left"],
            serial_number=["SN-1234"],
        )
        assert_matches_type(CalibrationList, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Miru) -> None:
        response = client.platform.calibrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = response.parse()
        assert_matches_type(CalibrationList, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Miru) -> None:
        with client.platform.calibrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = response.parse()
            assert_matches_type(CalibrationList, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCalibrations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMiru) -> None:
        calibration = await async_client.platform.calibrations.retrieve(
            calibration_id="cal_123",
        )
        assert_matches_type(Calibration, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncMiru) -> None:
        calibration = await async_client.platform.calibrations.retrieve(
            calibration_id="cal_123",
            expand=["content"],
        )
        assert_matches_type(Calibration, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMiru) -> None:
        response = await async_client.platform.calibrations.with_raw_response.retrieve(
            calibration_id="cal_123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = await response.parse()
        assert_matches_type(Calibration, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMiru) -> None:
        async with async_client.platform.calibrations.with_streaming_response.retrieve(
            calibration_id="cal_123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = await response.parse()
            assert_matches_type(Calibration, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMiru) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `calibration_id` but received ''"):
            await async_client.platform.calibrations.with_raw_response.retrieve(
                calibration_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMiru) -> None:
        calibration = await async_client.platform.calibrations.list()
        assert_matches_type(CalibrationList, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncMiru) -> None:
        calibration = await async_client.platform.calibrations.list(
            aspect=["pose"],
            component=["arm"],
            expand=["content"],
            limit=10,
            offset=0,
            order_by=["created_at:desc"],
            report_id=["0b6f3c2e-6a51-4e0f-9a43-2f1d7c9e8b10"],
            role=["front-left"],
            serial_number=["SN-1234"],
        )
        assert_matches_type(CalibrationList, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMiru) -> None:
        response = await async_client.platform.calibrations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        calibration = await response.parse()
        assert_matches_type(CalibrationList, calibration, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMiru) -> None:
        async with async_client.platform.calibrations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            calibration = await response.parse()
            assert_matches_type(CalibrationList, calibration, path=["response"])

        assert cast(Any, response.is_closed) is True
