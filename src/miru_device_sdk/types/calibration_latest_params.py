# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["CalibrationLatestParams"]


class CalibrationLatestParams(TypedDict, total=False):
    aspect: SequenceNotStr[str]
    """
    The aspect slugs to filter by; `null` matches calibrations reported without an
    aspect. Aspect slugs are unique only within a component, so filter by component
    too to match one component's aspect.
    """

    component: SequenceNotStr[str]
    """The component slugs to filter by."""

    role: SequenceNotStr[str]
    """The role slugs to filter by; `null` matches calibrations reported without a
    role.

    Role slugs are unique only within a component, so filter by component too to
    match one component's role.
    """
