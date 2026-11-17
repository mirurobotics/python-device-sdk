# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DeviceRetrieveResponse"]


class DeviceRetrieveResponse(BaseModel):
    id: str
    """ID of the device."""

    last_connected_secs_ago: Optional[int] = None
    """
    Seconds since the device last connected to the backend, as measured by the agent
    when it built this response, or null if it hasn't connected since the agent last
    started.
    """

    last_disconnected_secs_ago: Optional[int] = None
    """
    Seconds since the device last disconnected from the backend, as measured by the
    agent when it built this response, or null if it hasn't disconnected since the
    agent last started.
    """

    last_synced_secs_ago: Optional[int] = None
    """
    Seconds since the device last synced, as measured by the agent when it built
    this response, or null if it hasn't synced since the agent last started.
    """

    name: str
    """Name of the device."""

    object: Literal["device"]
    """The object type, which is always `device`."""

    status: Literal["online", "offline"]
    """The status of the device.

    - Online: The miru agent is connected
    - Offline: The miru agent is disconnected (e.g. network issues, device is
      powered off, etc.)
    """
