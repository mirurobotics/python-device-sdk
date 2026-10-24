# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FileRule", "Source", "Retention", "Upload"]


class Source(BaseModel):
    glob: str
    """
    Absolute glob of the files this rule manages (`/` on Linux, `C:\\……` or `C:/…` on
    Windows; max 1024 bytes; no `.`, `..` or empty segments). A `{name}` capture
    matches like `*` within one segment and must be used in `upload.bundle` or
    `upload.path`. Names match `[a-z][a-z0-9_]*`, are unique, and must not reuse a
    built-in path variable. A segment holds at most one capture, and the rest of
    that segment must be constant text (no `*`, `?`, `[`, `\\`` or other braces). A
    capture may not have `**` segments both before and after it. `{a,b}` is literal.
    Devices see each capture as `*`.
    """

    stability_window_secs: int
    """
    How long, in seconds, a matching file's size and modification time must stay
    unchanged (quiescent) before it is considered finished and eligible for upload.
    Files in a format with a finalization marker (e.g. MCAP, parquet) are detected
    directly; this window is the fallback for other files.
    """


class Retention(BaseModel):
    """
    The retention block a file rule carries when it deletes local files; a
    rule without one keeps matching files indefinitely and Miru never
    deletes them. Retention operates in two phases. The retention guarantee
    ends once a matching file goes quiescent — its size and modification
    time have stayed unchanged for `source.stability_window_secs` — and,
    when `require_upload` is `true`, once its upload has been durably
    confirmed; the file is then eligible for deletion, and callers may no
    longer rely on it being present. `ttl_secs` schedules the enforcement
    that follows: how long the file lives on after the guarantee ends
    before the device deletes it. Both phases keep running on the device
    even when no release is deployed, so tearing down a deployment does not
    silently stop reclaiming disk.
    """

    ttl_secs: int
    """How long, in seconds, the file lives on after it becomes eligible for deletion.

    The clock starts when the retention guarantee ends, not when the file was
    written: this schedules enforcement of a guarantee that has already ended, so it
    defers the deletion, not the end of the guarantee. `0` means the file is deleted
    as soon as it becomes eligible.
    """

    require_upload: Optional[bool] = None
    """Whether a file must have its upload durably confirmed before it may be deleted.

    Present exactly when the rule has an `upload` block. When `true`, a slow or
    failing upload keeps the local file: the device abandons an upload after 9
    attempts, so a permanently failing upload retains the file indefinitely. When
    `false`, the upload is best-effort: the file may be deleted once eligible even
    if its upload has not completed, and an unfinished upload is abandoned.
    """


class Upload(BaseModel):
    """Where matching files are uploaded.

    Absent when the rule only enforces local retention.
    """

    bucket_id: str
    """ID of the bucket this rule uploads to."""

    bucket_name: str
    """Name of the bucket this rule uploads to."""

    path: str
    """Object-path template for the uploaded file.

    Contains `{upload_id}`, is at most 1024 bytes, has balanced braces, and contains
    no `..` or empty segments. Variables: `{device_id}`, `{device_name}`,
    `{file_name}`, `{upload_id}`, `{bundle_id}`, `{year}`, `{month}`, `{day}`,
    `{hour}`, `{minute}`, `{timezone}`, plus any `source.glob` capture.
    `{bundle_id}` requires `bundle`. The time variables are zero-padded and rendered
    from the file's mtime (its last-modified time, from the device clock) in
    `timezone`; `{timezone}` is that instant's UTC offset in ISO 8601 basic format
    (`+0000`, `-0500`).
    """

    timezone: Literal["utc", "device"]
    """
    The time zone a file rule renders its upload path's time variables (`{year}`,
    `{month}`, `{day}`, `{hour}`, `{minute}` and `{timezone}`) in.

    - `utc`: Coordinated Universal Time.
    - `device`: the device's local time zone, as the agent resolves it from the `TZ`
      environment variable or, when `TZ` is unset, the system time zone
      (`/etc/localtime` on Linux). The UTC offset is taken at the rendered instant,
      so it follows daylight saving time. A device running an agent that does not
      report its UTC offset renders in UTC.
    """

    upload_collection_id: str
    """ID of the upload collection the resulting uploads are grouped into."""

    upload_collection_name: str
    """The name of the upload collection the resulting uploads are grouped into."""

    bundle: Optional[List[str]] = None
    """
    Names of the `source.glob` captures whose values group the rule's uploads into
    bundles: uploads from the same device and upload collection that captured the
    same values, in the order listed, share a bundle, across rules and over time.
    Capture names don't affect matching, so rules that name their captures
    differently still share a bundle when they list them in the same order. Every
    name must be a `source.glob` capture, listed once, with at most 16 names. Absent
    when the rule does not bundle.
    """


class FileRule(BaseModel):
    """
    A file rule declares which files on a device Miru manages and what to do
    with them: upload them to a bucket, delete the local copies once they
    are no longer needed, or both. `retention` is optional and marks the
    rules that delete: when it is absent the device keeps matching files
    indefinitely — Miru never deletes them — and when it is present the rule
    deletes each matching file once its retention guarantee ends. A rule
    that both deletes and uploads always states `retention.require_upload`,
    so whether local deletion waits for the upload is itself an explicit
    decision.
    """

    id: str
    """ID of the file rule."""

    created_at: datetime
    """Timestamp of when the file rule was created."""

    digest: str
    """The digest of the file rule.

    File rules are immutable and deduplicated by digest within a workspace.
    """

    name: str
    """A human-readable name for the file rule.

    Not unique within a workspace: file rules are immutable, so each authored
    revision mints a new rule and several rules may share a name. The name
    participates in the rule's digest, so renaming a rule mints a new rule.
    """

    object: Literal["file_rule"]
    """The object type, which is always `file_rule`."""

    os: Literal["linux", "windows"]
    """An operating system family, from the agent's build-time OS vocabulary.

    Shared across resources (devices, config schemas, file rules, releases). This is
    the machine-readable OS kind, distinct from a human-readable version string.

    - `linux`
    - `windows`
    """

    source: Source

    updated_at: datetime
    """Timestamp of when the file rule was last updated."""

    retention: Optional[Retention] = None
    """
    The retention block a file rule carries when it deletes local files; a rule
    without one keeps matching files indefinitely and Miru never deletes them.
    Retention operates in two phases. The retention guarantee ends once a matching
    file goes quiescent — its size and modification time have stayed unchanged for
    `source.stability_window_secs` — and, when `require_upload` is `true`, once its
    upload has been durably confirmed; the file is then eligible for deletion, and
    callers may no longer rely on it being present. `ttl_secs` schedules the
    enforcement that follows: how long the file lives on after the guarantee ends
    before the device deletes it. Both phases keep running on the device even when
    no release is deployed, so tearing down a deployment does not silently stop
    reclaiming disk.
    """

    upload: Optional[Upload] = None
    """Where matching files are uploaded.

    Absent when the rule only enforces local retention.
    """
