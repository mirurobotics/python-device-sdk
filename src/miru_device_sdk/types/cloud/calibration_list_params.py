# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CalibrationListParams"]


class CalibrationListParams(TypedDict, total=False):
    aspect: SequenceNotStr[str]
    """
    The aspect slugs to filter by; `null` matches calibrations reported without an
    aspect. Aspect slugs are unique only within a component, so filter by component
    too to match one component's aspect.
    """

    component: SequenceNotStr[str]
    """The component slugs to filter by."""

    expand: List[Literal["content", "total_count"]]
    """Fields to expand on each calibration in the list."""

    limit: int
    """The maximum number of items to return.

    A limit of 15 with an offset of 0 returns items 1-15.
    """

    offset: int
    """The offset of the items to return.

    An offset of 10 with a limit of 10 returns items 11-20.
    """

    order_by: List[
        Literal["id:asc", "id:desc", "created_at:asc", "created_at:desc", "reported_at:asc", "reported_at:desc"]
    ]
    """Sort order for the calibration results."""

    report_id: SequenceNotStr[str]
    """The report IDs to filter by."""

    role: SequenceNotStr[str]
    """The role slugs to filter by; `null` matches calibrations reported without a
    role.

    Role slugs are unique only within a component, so filter by component too to
    match one component's role.
    """

    serial_number: SequenceNotStr[str]
    """The unit serial numbers to filter by."""
