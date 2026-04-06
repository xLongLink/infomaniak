from __future__ import annotations

from typing import Any, Literal
from dataclasses import dataclass


@dataclass(slots=True)
class PublicCloudTag:
    """User-defined tag attached to a public cloud product."""

    id: int
    name: str
    color: int
    product_count: int | None = None


@dataclass(slots=True)
class PublicCloudRights:
    """Access rights attached to a public cloud product."""

    technical: bool | None = None
    statistic: bool | None = None
    check: bool | None = None
    sale: bool | None = None


@dataclass(slots=True)
class PublicCloudStatus:
    """Status payload of a public cloud product."""

    maintenance: bool
    locked: bool
    activated_by: int | None
    activated_at: int | None


@dataclass(slots=True)
class PublicCloudData:
    """Billing and usage details for a public cloud product."""

    price: float | None
    price_updated_at: int | None
    updated_at: int
    billing_start_at: int
    billing_end_at: int
    project_count: int


@dataclass(slots=True)
class PublicCloud:
    """Public cloud product payload."""

    id: int
    account_id: int
    service_id: int
    service_name: str
    customer_name: str
    internal_name: str | None
    created_at: int
    expired_at: int | None
    version: int
    has_maintenance: bool
    is_locked: bool
    has_operation_in_progress: bool
    tags: list[PublicCloudTag]
    unique_id: int
    is_free: bool
    is_zero_price: bool
    is_trial: bool
    rights: PublicCloudRights
    public_cloud_id: int
    public_cloud: PublicCloudData
    deleted_at: int | None = None
    description: str | None = None
    bill_reference: str | None = None
    parent_id: int | None = None
    parent_service_id: int | None = None
    parent_service_name: str | None = None
    status: PublicCloudStatus | None = None
    users: list[dict[str, Any]] | None = None
    admin: dict[str, Any] | None = None
    fqdn: str | None = None


@dataclass(slots=True)
class PublicCloudBoolResponse:
    """Boolean API response wrapper for public cloud operations."""

    result: Literal["asynchronous", "delayed", "success", "error"]
    data: bool | str
