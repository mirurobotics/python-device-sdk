# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .calibration import Calibration

__all__ = ["CalibrationLatestResponse"]


class CalibrationLatestResponse(BaseModel):
    calibrations: List[Calibration]
    """The latest calibrations, one for each component, role and aspect."""

    is_confirmed: bool
    """Whether the list includes the device's calibrations from Miru.

    Until it does, `calibrations` holds only calibrations reported to this agent.
    """
