from __future__ import annotations

from typing import Literal
from dataclasses import dataclass


@dataclass(slots=True)
class ChkShortUrl:
    """Short URL payload."""

    code: str
    url: str
    created_at: int
    expiration_date: int | None = None


@dataclass(slots=True)
class ChkShortUrlResponse:
    """Create or update short URL response payload."""

    result: Literal["success", "error", "asynchronous"]
    data: ChkShortUrl


@dataclass(slots=True)
class ChkQuota:
    """Short URL quota payload."""

    quota: int
    limit: int
