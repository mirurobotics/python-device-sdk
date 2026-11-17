# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AgentSyncResponse"]


class AgentSyncResponse(BaseModel):
    code: Literal["success", "network_connection_error", "in_cooldown"]
    """The result of attempting to sync the device."""

    cooldown_ends_in_secs: int
    """
    Seconds until the cooldown ends, rounded up, as measured by the agent when it
    built this response. `0` exactly when `in_cooldown` is false.
    """

    in_cooldown: bool
    """Whether the device is currently in cooldown."""

    last_attempted_sync_secs_ago: int
    """
    Seconds since the device last _attempted_ to sync, as measured by the agent when
    it built this response.
    """

    last_synced_secs_ago: Optional[int] = None
    """
    Seconds since the device last synced, as measured by the agent when it built
    this response, or null if it hasn't synced since the agent last started.
    """

    message: str
    """The message of the result."""
