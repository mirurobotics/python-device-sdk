# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["EventStreamParams"]


class EventStreamParams(TypedDict, total=False):
    after: int
    """Event ID cursor to resume from.

    Retained events with `id` greater than this value are replayed, then live events
    follow. If the cursor is older than the earliest retained event, the server
    returns `410 Gone`. Takes precedence over the `Last-Event-ID` header.
    """

    types: SequenceNotStr[str]
    """Event types to receive. If omitted, all event types are sent."""

    last_event_id: Annotated[str, PropertyInfo(alias="Last-Event-ID")]
