from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class BackupProduct:
    """Placeholder model for Swiss Backup product payloads."""

    id: int
    name: str
    status: str | None = None


@dataclass(slots=True)
class BackupSlot:
    """Placeholder model for Swiss Backup slot payloads."""

    id: int
    label: str
    enabled: bool


@dataclass(slots=True)
class BackupBillingPlan:
    """Placeholder model for Swiss Backup billing plan payloads."""

    product: str
    currency: str
    price: float
    discount: float | None = None
