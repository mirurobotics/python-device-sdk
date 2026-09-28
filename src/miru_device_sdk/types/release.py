# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Release"]


class Release(BaseModel):
    id: str
    """ID of the release."""

    created_at: datetime
    """Timestamp of when the release was created."""

    file_rule_ids: List[str]
    """IDs of the file rules included in this release.

    Retrieve each file rule with `GET /file_rules/{file_rule_id}`.
    """

    git_commit_id: Optional[str] = None
    """The ID of the git commit associated with this release."""

    object: Literal["release"]
    """The object type, which is always `release`."""

    os: Literal["linux", "windows"]
    """An operating system family, from the agent's build-time OS vocabulary.

    Shared across resources (devices, config schemas, file rules, releases). This is
    the machine-readable OS kind, distinct from a human-readable version string.

    - `linux`
    - `windows`
    """

    version: str
    """The version of the release."""
