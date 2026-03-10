# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Deployment"]


class Deployment(BaseModel):
    id: str
    """ID of the deployment."""

    activity_status: Literal["drifted", "staged", "queued", "deployed", "archived"]
    """Last known activity state of the deployment.

    `drifted` means the device's configurations have drifted since this deployment
    was staged, and the deployment needs to be reviewed before it can be deployed.

    `staged` means the deployment is ready to be deployed.

    `queued` means the deployment's config instances are waiting to be received by
    the device and will be deployed as soon as the device is online.

    `deployed` means the deployment's config instances are currently available for
    consumption on the device.

    `archived` means the deployment is available for historical reference but cannot
    be deployed and is not active on the device.
    """

    created_at: datetime
    """Timestamp of when the device release was created."""

    description: str
    """The description of the deployment."""

    device_id: str
    """ID of the device."""

    error_status: Literal["none", "failed", "retrying"]
    """Last known error state of the deployment.

    `none` means there are no errors.

    `retrying` means an error has been encountered and the agent is retrying to
    reach the target status.

    `failed` means a fatal error has been encountered; the deployment is archived
    and, if deployed, removed from the device.
    """

    object: Literal["deployment"]
    """The object type, which is always `deployment`."""

    release_id: str
    """ID of the release."""

    status: Literal["drifted", "staged", "queued", "deployed", "archived", "failed", "retrying"]
    """
    This status merges the 'activity_status' and 'error_status' fields, with error
    states taking precedence over activity states when errors are present. For
    example, if the activity status is 'deployed' but the error status is 'failed',
    the status is 'failed'. However, if the error status is 'none' and the activity
    status is 'deployed', the status is 'deployed'.
    """

    target_status: Literal["staged", "deployed", "archived"]
    """Desired state of the deployment.

    `staged` means the deployment is ready to be deployed.

    `deployed` means all config instances in the deployment are available for
    consumption on the device.

    `archived` means the deployment is available for historical reference but cannot
    be deployed and is not active on the device.
    """
