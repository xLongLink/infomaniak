from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


@dataclass(slots=True)
class DNSSECInfo:
    """DNSSEC information for a zone."""

    is_enabled: bool


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


@dataclass(slots=True)
class DNSZone:
    """
    DNS zone payload.

    OpenAPI schema: `2f8071fd_api_dns_zone`.
    """

    id: int
    fqdn: str
    dnssec: DNSSECInfo
    nameservers: list[str]
    skel: str | None = None
    records: list[DNSRecord] | None = None
