# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Calibration"]


class Calibration(BaseModel):
    """The newest calibration the device has for one component."""

    component: str
    """Slug of the component the calibrated unit belongs to."""

    invalidated_at: Optional[datetime] = None
    """
    Timestamp of when a device app marked this calibration invalid, or null if it is
    valid. A newer calibration for the component replaces it.
    """

    object: Literal["calibration"]
    """The object type, which is always `calibration`."""

    report_id: str
    """ID the agent gave the report this calibration came from.

    Download the content with it.
    """

    reported_at: datetime
    """Timestamp of when the agent received the calibration."""

    reported_by: Optional[str] = None
    """
    Who reported the calibration, as it was reported, such as `Benjamin Smidt`; null
    if no one was reported.
    """

    serial_number: Optional[str] = None
    """
    Serial number of the physical unit that was calibrated, not of the device, such
    as `SN-1234`, or null if none was reported. Free text, at most 255 characters.
    """
