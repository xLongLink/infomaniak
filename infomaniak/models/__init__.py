"""SDK models."""

from infomaniak.models.backup import (
    BackupBillingPlan,
    BackupProduct,
    BackupSlot,
)
from infomaniak.models.core.user import (
    AccountInvitation,
    AccountInvitationTeam,
)
from infomaniak.models.dns import DNSRecord, DNSZone
from infomaniak.models.domain import Domain, DomainListResponse
from infomaniak.models.newsletter import NewsletterBulkResponse

__all__ = [
    "BackupProduct",
    "BackupSlot",
    "BackupBillingPlan",
    "AccountInvitation",
    "AccountInvitationTeam",
    "DNSRecord",
    "DNSZone",
    "Domain",
    "DomainListResponse",
    "NewsletterBulkResponse",
]
