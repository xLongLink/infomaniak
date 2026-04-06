from __future__ import annotations

from typing import Literal
from infomaniak.utils import parse, plist
from infomaniak.resource import Resouce, AsyncResource
from infomaniak.models.dns.zone import DNSRecord

DNSRecordType = Literal[
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


class Records(Resouce):
    """DNS zone records endpoints."""

    def list(
        self,
        zone: str,
        *,
        source: str | None = None,
        types: list[DNSRecordType] | None = None,
        search: str | None = None,
        with_: str | None = None,
        page: int | None = None,
        items: int | None = None,
        order_by: (
            Literal[
                "id",
                "source_idn",
                "target",
                "type",
                "ttl",
                "updated_at",
            ]
            | None
        ) = None,
        order: Literal["asc", "desc"] | None = None,
    ) -> plist[DNSRecord]:
        """Retrieve all DNS records for a given zone."""
        url = f"/2/zones/{zone}/records"
        params: dict[str, str | int | list[str]] = {}

        if source is not None:
            params["filter[source]"] = source
        if types is not None:
            params["filter[types][]"] = types
        if search is not None:
            params["search"] = search
        if with_ is not None:
            params["with"] = with_
        if page is not None:
            params["page"] = page
        if items is not None:
            params["items"] = items
        if order_by is not None:
            params["order_by"] = order_by
        if order is not None:
            params["order"] = order

        response = self._client.get(url, params=params or None)
        payload = response.json()
        return plist(
            [parse(DNSRecord, record) for record in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    def store(
        self,
        zone: str,
        target: str,
        ttl: int,
        type_: DNSRecordType,
        *,
        source: str | None = None,
        with_: str | None = None,
    ) -> DNSRecord:
        """Create a DNS record in a given zone."""
        url = f"/2/zones/{zone}/records"
        params = {"with": with_} if with_ is not None else None
        payload: dict[str, str | int] = {
            "target": target,
            "ttl": ttl,
            "type": type_,
        }
        if source is not None:
            payload["source"] = self._normalize_source(zone, source)
        response = self._client.post(url, json=payload, params=params)
        return parse(DNSRecord, response.json()["data"])

    def display(self, zone: str, record: int) -> DNSRecord:
        """Retrieve one DNS record for a given zone."""
        url = f"/2/zones/{zone}/records/{record}"
        response = self._client.get(url)
        return parse(DNSRecord, response.json()["data"])

    def update(
        self,
        zone: str,
        record: int,
        target: str,
        ttl: int,
        *,
        with_: str | None = None,
    ) -> DNSRecord:
        """Update a DNS record."""
        url = f"/2/zones/{zone}/records/{record}"
        params = {"with": with_} if with_ is not None else None
        response = self._client.put(
            url,
            json={"target": target, "ttl": ttl},
            params=params,
        )
        return parse(DNSRecord, response.json()["data"])

    def delete(self, zone: str, record: int) -> bool:
        """Delete a DNS record."""
        url = f"/2/zones/{zone}/records/{record}"
        response = self._client.delete(url)
        return bool(response.json()["data"])

    def check(self, zone: str, record: int) -> bool:
        """Verify that a DNS record exists and resolves."""
        url = f"/2/zones/{zone}/records/{record}/check"
        response = self._client.get(url)
        return bool(response.json()["data"])

    def match(
        self,
        zone: str,
        source: str,
        type_: DNSRecordType,
        target: str,
        ttl: int = 3600,
    ) -> DNSRecord:
        """Ensure one DNS record exists with the expected target and TTL."""
        normalized_source = self._normalize_source(zone, source)
        records = self.list(zone, source=normalized_source, types=[type_])
        for record in records:
            if record.source == normalized_source and record.type == type_:
                if record.target != target or record.ttl != ttl:
                    return self.update(zone, record.id, target, ttl)
                return record
        return self.store(
            zone,
            target,
            ttl,
            type_,
            source=normalized_source,
        )

    @staticmethod
    def _normalize_source(zone: str, source: str) -> str:
        suffix = f".{zone}"
        if source.endswith(suffix):
            return source.removesuffix(suffix)
        return source


class AsyncRecords(AsyncResource):
    """Async DNS zone records endpoints."""

    async def list(
        self,
        zone: str,
        *,
        source: str | None = None,
        types: list[DNSRecordType] | None = None,
        search: str | None = None,
        with_: str | None = None,
        page: int | None = None,
        items: int | None = None,
        order_by: (
            Literal[
                "id",
                "source_idn",
                "target",
                "type",
                "ttl",
                "updated_at",
            ]
            | None
        ) = None,
        order: Literal["asc", "desc"] | None = None,
    ) -> plist[DNSRecord]:
        """Retrieve all DNS records for a given zone."""
        url = f"/2/zones/{zone}/records"
        params: dict[str, str | int | list[str]] = {}

        if source is not None:
            params["filter[source]"] = source
        if types is not None:
            params["filter[types][]"] = types
        if search is not None:
            params["search"] = search
        if with_ is not None:
            params["with"] = with_
        if page is not None:
            params["page"] = page
        if items is not None:
            params["items"] = items
        if order_by is not None:
            params["order_by"] = order_by
        if order is not None:
            params["order"] = order

        response = await self._client.get(url, params=params or None)
        payload = response.json()
        return plist(
            [parse(DNSRecord, record) for record in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    async def store(
        self,
        zone: str,
        target: str,
        ttl: int,
        type_: DNSRecordType,
        *,
        source: str | None = None,
        with_: str | None = None,
    ) -> DNSRecord:
        """Create a DNS record in a given zone."""
        url = f"/2/zones/{zone}/records"
        params = {"with": with_} if with_ is not None else None
        payload: dict[str, str | int] = {
            "target": target,
            "ttl": ttl,
            "type": type_,
        }
        if source is not None:
            payload["source"] = self._normalize_source(zone, source)
        response = await self._client.post(url, json=payload, params=params)
        return parse(DNSRecord, response.json()["data"])

    async def display(self, zone: str, record: int) -> DNSRecord:
        """Retrieve one DNS record for a given zone."""
        url = f"/2/zones/{zone}/records/{record}"
        response = await self._client.get(url)
        return parse(DNSRecord, response.json()["data"])

    async def update(
        self,
        zone: str,
        record: int,
        target: str,
        ttl: int,
        *,
        with_: str | None = None,
    ) -> DNSRecord:
        """Update a DNS record."""
        url = f"/2/zones/{zone}/records/{record}"
        params = {"with": with_} if with_ is not None else None
        response = await self._client.put(
            url,
            json={"target": target, "ttl": ttl},
            params=params,
        )
        return parse(DNSRecord, response.json()["data"])

    async def delete(self, zone: str, record: int) -> bool:
        """Delete a DNS record."""
        url = f"/2/zones/{zone}/records/{record}"
        response = await self._client.delete(url)
        return bool(response.json()["data"])

    async def check(self, zone: str, record: int) -> bool:
        """Verify that a DNS record exists and resolves."""
        url = f"/2/zones/{zone}/records/{record}/check"
        response = await self._client.get(url)
        return bool(response.json()["data"])

    async def match(
        self,
        zone: str,
        source: str,
        type_: DNSRecordType,
        target: str,
        ttl: int = 3600,
    ) -> DNSRecord:
        """Ensure one DNS record exists with the expected target and TTL."""
        normalized_source = self._normalize_source(zone, source)
        records = await self.list(zone, source=normalized_source, types=[type_])
        for record in records:
            if record.source == normalized_source and record.type == type_:
                if record.target != target or record.ttl != ttl:
                    return await self.update(zone, record.id, target, ttl)
                return record
        return await self.store(
            zone,
            target,
            ttl,
            type_,
            source=normalized_source,
        )

    @staticmethod
    def _normalize_source(zone: str, source: str) -> str:
        suffix = f".{zone}"
        if source.endswith(suffix):
            return source.removesuffix(suffix)
        return source
