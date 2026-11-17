# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CalibrationInvalidateParams"]


class CalibrationInvalidateParams(TypedDict, total=False):
    component: Required[str]
    """Slug of the component whose latest calibration to invalidate, such as `arm`."""

    reason: Required[str]
    """Why the calibration is no longer valid, such as `power cycle`.

    Free text, at most 512 characters, and not blank.
    """

    report_id: str
    """Report ID of the calibration the caller expects to be `component`'s latest.

    If it is not `component`'s current latest calibration, the agent invalidates
    nothing. Leave it out to invalidate whatever is latest.
    """
