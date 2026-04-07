# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Event"]


class Event(BaseModel):
    id: int
    """Monotonically increasing event ID.

    Used as the SSE `id` field and for replay cursors.
    """

    data: object
    """Event-specific payload. Shape varies by event type."""

    object: Literal["event"]
    """The object type, which is always `event`."""

    occurred_at: datetime
    """Timestamp of when the event occurred."""

    type: str
    """Event type string in the format `{resource}.{action}`."""
