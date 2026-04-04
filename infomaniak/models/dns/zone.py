from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass(slots=True)
class DNSRecord:
    """
    DNS record payload.

    OpenAPI schema: `2f8071fd_api_dns_dns_record`.
    """

    id: int
    source: str
    target: str
    ttl: int
    type: Literal[
        "A",
        "AAAA",
        "CAA",
        "CNAME",
        "DNAME",
        "DNSKEY",
        "DS",
        "MX",
        "NS",
        "PTR",
        "SMIMEA",
        "SOA",
        "SRV",
        "SSHFP",
        "TLSA",
        "TXT",
    ]
    updated_at: int
    source_idn: str | None = None
    dyndns_id: int | None = None
    delegated_zone: dict[str, object] | None = None
    description: dict[str, object] | None = None
