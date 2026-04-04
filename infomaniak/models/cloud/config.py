from __future__ import annotations

from typing import Literal
from dataclasses import dataclass


@dataclass(slots=True)
class PublicCloudConfig:
    """Public cloud configuration payload."""

    free_tier: float
    free_tier_used: float
    account_resource_level: Literal[1, 2, 3, 4]
    valid_from: int
    valid_to: int
    project_count: int


@dataclass(slots=True)
class PublicCloudConfigResponse:
    """Get public cloud configuration response payload."""

    result: Literal["success", "error", "asynchronous"]
    data: PublicCloudConfig
