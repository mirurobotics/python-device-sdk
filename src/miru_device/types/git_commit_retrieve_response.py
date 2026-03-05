# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["GitCommitRetrieveResponse"]


class GitCommitRetrieveResponse(BaseModel):
    id: str
    """ID of the git commit."""

    commit_url: str
    """The URL of the git commit."""

    created_at: datetime
    """Timestamp of when the git commit was created."""

    message: str
    """The commit message."""

    object: Literal["git_commit"]
    """The object type, which is always `git_commit`."""

    sha: str
    """The SHA hash of the git commit."""
