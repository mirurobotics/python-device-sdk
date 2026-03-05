# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from .._models import BaseModel

__all__ = ["AgentVersionResponse"]


class AgentVersionResponse(BaseModel):
    api_git_commit: str
    """The git commit of the API."""

    api_version: str
    """The API version of the agent."""

    arch: str
    """The architecture of the agent."""

    build_date: datetime
    """The build date of the agent."""

    git_commit: str
    """The git commit of the agent."""

    os: str
    """The operating system of the agent."""

    rust_version: str
    """The version of Rust."""

    version: str
    """The version of the agent."""
