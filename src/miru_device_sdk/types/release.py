# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Release"]


class Release(BaseModel):
    id: str
    """ID of the release."""

    created_at: datetime
    """Timestamp of when the release was created."""

    git_commit_id: Optional[str] = None
    """The ID of the git commit associated with this release."""

    object: Literal["release"]
    """The object type, which is always `release`."""

    updated_at: datetime
    """Timestamp of when the release was last updated."""

    version: str
    """The version of the release."""
