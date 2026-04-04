from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Literal


@dataclass(slots=True)
class PublicCloudProjectTag:
    """User-defined tag attached to a public cloud project."""

    id: int
    name: str
    color: int


@dataclass(slots=True)
class PublicCloudProject:
    """Public cloud project payload."""

    public_cloud_project_id: int
    public_cloud_id: int
    open_stack_name: str
    name: str
    price: float
    resource_level: int
    status: Literal["creating", "deleting", "disabled", "disabling", "error", "ok", "updating"]
    price_updated_at: int
    billing_start_at: int
    billing_end_at: int
    created_at: int
    updated_at: int
    user_count: int
    tags: list[PublicCloudProjectTag]
    meta: list[Any]
    services: list[dict[str, Any]] | None = None


@dataclass(slots=True)
class CreatePublicCloudProjectResponse:
    """Create public cloud project response payload."""

    result: Literal["asynchronous", "delayed", "success", "error"]
    data: int | str


@dataclass(slots=True)
class PublicCloudProjectAsyncActionResponse:
    """Async action response payload for project update and deletion."""

    result: Literal["asynchronous", "delayed", "success", "error"]
    data: bool | str


@dataclass(slots=True)
class PublicCloudProjectInvitationResponse:
    """Create public cloud project invitation response payload."""

    result: Literal["asynchronous", "delayed", "success", "error"]
    data: int | str


@dataclass(slots=True)
class PublicCloudProjectListResponse:
    """List public cloud projects response payload with pagination metadata."""

    data: list[PublicCloudProject]
    total: int | None = None
    page: int | None = None
    pages: int | None = None
    items_per_page: int | None = None
