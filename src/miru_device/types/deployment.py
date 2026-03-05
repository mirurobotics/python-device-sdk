# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Deployment", "ConfigInstance", "ConfigInstanceContent"]


class ConfigInstanceContent(BaseModel):
    """The configuration values associated with the config instance."""

    data: str
    """The configuration values associated with the config instance."""

    format: Literal["json"]


class ConfigInstance(BaseModel):
    id: str
    """ID of the config instance."""

    config_schema_id: str
    """ID of the config schema which the config instance must adhere to."""

    config_type_id: str
    """ID of the config type which the config instance (and its schema) is a part of."""

    config_type_name: str
    """The name of the config type."""

    content: ConfigInstanceContent
    """The configuration values associated with the config instance."""

    created_at: datetime
    """The timestamp of when the config instance was created."""

    filepath: str
    """
    The file path to deploy the config instance relative to
    `/srv/miru/config_instances`. `v1/motion-control.json` would deploy to
    `/srv/miru/config_instances/v1/motion-control.json`.
    """

    object: Literal["config_instance"]
    """The object type, which is always `config_instance`."""


class Deployment(BaseModel):
    id: str
    """ID of the deployment."""

    activity_status: Literal["drifted", "staged", "queued", "deployed", "archived"]
    """Last known activity state of the deployment.

    - Drifted: device's configurations have drifted since this deployment was
      staged, and the deployment needs to be reviewed before it can be deployed
    - Staged: is ready to be deployed
    - Queued: the deployment's config instances are waiting to be received by the
      device; will be deployed as soon as the device is online
    - Deployed: the deployment's config instances are currently available for
      consumption on the device
    - Archived: the deployment is available for historical reference but cannot be
      deployed and is not active on the device
    """

    created_at: datetime
    """Timestamp of when the device release was created."""

    description: str
    """The description of the deployment."""

    device_id: str
    """ID of the device."""

    error_status: Literal["none", "failed", "retrying"]
    """Last known error state of the deployment.

    - None: no errors
    - Retrying: an error has been encountered and the agent is retrying to reach the
      target status
    - Failed: a fatal error has been encountered; the deployment is archived and (if
      deployed) removed from the device
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

    - Staged: is ready to be deployed
    - Deployed: all config instances part of the deployment are available for
      consumption on the device
    - Archived: the deployment is available for historical reference but cannot be
      deployed and is not active on the device
    """

    updated_at: datetime
    """Timestamp of when the device release was last updated."""

    config_instances: Optional[List[ConfigInstance]] = None
    """The config instances associated with this deployment."""
