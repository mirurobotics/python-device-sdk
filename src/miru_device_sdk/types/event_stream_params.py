# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EventStreamParams"]


class EventStreamParams(TypedDict, total=False):
    after: int
    """Event ID cursor.

    Only events with `id` greater than this value are returned. Takes precedence
    over the `Last-Event-ID` header.
    """

    types: SequenceNotStr[str]
    """Event types to receive. If omitted, all event types are sent."""

    last_event_id: Annotated[str, PropertyInfo(alias="Last-Event-ID")]
