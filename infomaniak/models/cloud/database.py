from __future__ import annotations

from typing import Any, Literal
from dataclasses import dataclass


@dataclass(slots=True)
class DatabaseServiceProject:
    """Public cloud project attached to a database service."""

    id: int
    public_cloud_id: int
    name: str
    open_stack_name: str


@dataclass(slots=True)
class DatabaseServicePack:
    """Database service pack details."""

    id: int
    type: str
    group: str
    name: str
    instances: int
    cpu: int
    ram: int
    storage: int
    rates: list[dict[str, Any]]


@dataclass(slots=True)
class DatabaseServiceTag:
    """Tag attached to a database service."""

    id: int
    name: str
    color: int
    product_count: int | None = None


@dataclass(slots=True)
class DatabaseServiceBackupSchedule:
    """Scheduled backup payload for a database service."""

    id: int
    scheduled_at: str
    retention: int
    is_pitr_enabled: bool
    name: str | None = None


@dataclass(slots=True)
class DatabaseServiceBackup:
    """Backup payload for a database service."""

    id: str
    location: str
    endpoint: str
    created_at: int
    status: str
    completed_at: int | None = None


@dataclass(slots=True)
class DatabaseService:
    """Database service payload."""

    id: int
    kube_cluster: str
    kube_identifier: str
    name: str
    region: str
    type: str
    version: str
    status: Literal["error", "initializing", "paused", "ready", "stopping", "unknown"] | None = None
    project: DatabaseServiceProject | None = None
    pack: DatabaseServicePack | None = None
    tags: list[DatabaseServiceTag] | None = None
    connection: list[dict[str, Any]] | None = None
    backup_schedules: list[DatabaseServiceBackupSchedule] | None = None
    configuration: list[dict[str, Any]] | None = None
    backups: list[DatabaseServiceBackup] | None = None
    last_backup_at: int | None = None
    total_backup_size: int | None = None


@dataclass(slots=True)
class DatabaseServiceListResponse:
    """List database services response payload with pagination metadata."""

    data: list[DatabaseService]
    total: int | None = None
    page: int | None = None
    pages: int | None = None
    items_per_page: int | None = None


@dataclass(slots=True)
class DatabaseServiceCreation:
    """Database service creation payload."""

    id: int
    admin_password: str
    kube_identifier: str


@dataclass(slots=True)
class DatabaseServiceCreationResponse:
    """Response payload returned by database service creation operations."""

    result: Literal["success", "error", "asynchronous"]
    data: DatabaseServiceCreation


@dataclass(slots=True)
class DatabaseServiceConnection:
    """Connection payload returned by database password reset operations."""

    host: str
    port: str
    user: str
    password: str
    uri: str
    command: str
    ca: str


@dataclass(slots=True)
class DatabaseServiceConnectionResponse:
    """Response payload returned by database service password reset operations."""

    result: Literal["success", "error", "asynchronous"]
    data: DatabaseServiceConnection


@dataclass(slots=True)
class DatabaseServiceBoolResponse:
    """Response payload for boolean database service operations."""

    result: Literal["success", "error", "asynchronous"]
    data: bool


@dataclass(slots=True)
class CreateDatabaseServiceBackupScheduleRequest:
    """Create database service backup schedule request payload."""

    add_default_schedule: bool | None = None
    is_pitr_enabled: bool | None = None
    retention: int | None = None
    scheduled_at: str | None = None
