# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["CalibrationCreateResponse"]


class CalibrationCreateResponse(BaseModel):
    report_id: str
    """ID the agent gave this report.

    The agent sends it to Miru with the calibration, and Miru stores it as the
    calibration's `report_id`.
    """

    reported_at: datetime
    """Timestamp of when the agent received the calibration.

    Miru stores it as the time the calibration was reported.
    """
