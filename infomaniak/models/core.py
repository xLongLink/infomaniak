from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class Timezone:
    """Timezone payload."""

    id: int
    name: str
    gmt: str
