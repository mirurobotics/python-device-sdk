# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Calibration"]


class Calibration(BaseModel):
    """
    The newest calibration the device has for one component, role and aspect, uploaded or not.
    """

    aspect: Optional[str] = None
    """
    Slug of the aspect of the unit that was calibrated, as it was reported; null if
    no aspect was reported.
    """

    component: str
    """Slug of the component the calibrated unit belongs to, as it was reported."""

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

    role: Optional[str] = None
    """
    Slug of the role the calibrated unit fills on the device, as it was reported;
    null if no role was reported.
    """

    serial_number: Optional[str] = None
    """
    Serial number of the physical unit that was calibrated, not of the device, such
    as `SN-1234`, or null if none was reported. Free text, at most 255 characters.
    """

    upload_status: Literal["queued", "uploaded", "dropped"]
    """Whether the agent has uploaded the calibration to Miru.

    - `queued`: the agent will upload it once it can reach Miru.
    - `uploaded`: Miru has recorded it.
    - `dropped`: the agent gave up uploading it. The device still uses it, but Miru
      never recorded it.
    """
