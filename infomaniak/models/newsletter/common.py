from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class NewsletterBulkResponse:
    """Shared response model for newsletter bulk operations."""

    success: bool
    message: str | None = None
