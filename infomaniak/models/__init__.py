"""SDK models."""

from infomaniak.models.core.user import (
    AccountInvitation,
    AccountInvitationTeam,
)
from infomaniak.models.newsletter import NewsletterBulkResponse

__all__ = [
    "AccountInvitation",
    "AccountInvitationTeam",
    "NewsletterBulkResponse",
]
