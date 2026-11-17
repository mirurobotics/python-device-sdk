# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["CalibrationLatestParams"]


class CalibrationLatestParams(TypedDict, total=False):
    component: SequenceNotStr[str]
    """The component slugs to filter by."""
