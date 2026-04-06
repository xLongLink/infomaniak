from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Timezone:
    """Timezone payload."""

    id: int
    name: str
    gmt: str


@dataclass(slots=True)
class Country:
    """Country payload."""

    id: int
    name: str
    short_name: str
    is_enabled: bool
