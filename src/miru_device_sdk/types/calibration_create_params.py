# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["CalibrationCreateParams", "Content"]


class CalibrationCreateParams(TypedDict, total=False):
    component_slug: Required[str]
    """Slug of the component the calibrated unit belongs to.

    A new slug creates a component in Miru.
    """

    content: Required[Content]
    """The calibration's content, at most 1 MiB.

    The agent uploads it to Miru unchanged.
    """

    aspect: str
    """
    Slug of the aspect of the unit that was calibrated, when it has more than one,
    e.g. `intrinsics` vs `extrinsics`, or `pose` vs `home-offsets`. Validated like a
    slug. Miru resolves it to one of the component's `aspects`, creating the aspect
    the first time it is reported.
    """

    role: str
    """
    Slug of the role the calibrated unit fills on the device, such as `aligner-1` or
    `front-left`. Distinguishes several units of one component on a device.
    Validated like a slug. Miru resolves it to one of the component's `roles`,
    creating the role the first time it is reported.
    """

    serial_number: str
    """
    Serial number of the physical unit that was calibrated, not of the device, such
    as `M500-1234`. Free text, at most 255 characters.
    """


class Content(TypedDict, total=False):
    """The calibration's content, at most 1 MiB.

    The agent uploads it to Miru unchanged.
    """

    data: Required[str]
    """The content's values, serialized in `format`."""

    format: Required[Literal["json", "yaml", "jsonc", "xml", "text"]]
    """The serialization format of config content.

    A config instance is written to the device filesystem in this format.

    - `json`: standard JSON.
    - `yaml`: YAML 1.2.
    - `jsonc`: JSON with comments (JSON plus `//` and `/* */` comment syntax).
    - `xml`: XML.
    - `text`: plain, unstructured text with no specific format.
    """
