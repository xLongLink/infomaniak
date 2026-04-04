from __future__ import annotations

from dacite import from_dict
from typing import Any
from .records import Records, AsyncRecords
from infomaniak.utils import _with
from infomaniak.resource import Resouce, AsyncResource
from infomaniak.models.dns.zone import DNSZone


def _build_with_values(
    *,
    skel: bool,
    records: bool,
    records_description: bool,
    idn: bool,
    label: bool = False,
) -> str | None:
    return _with(
        skel=skel,
        records=records,
        records_description=records_description,
        idn=idn,
        label=label,
    )


def _extract_zone_payload(
    payload: dict[str, Any],
) -> dict[str, Any]:
    """Normalize DNS zone responses that may be wrapped or returned directly."""
    data = payload.get("data")
    if isinstance(data, dict):
        return data
    return payload


class Zone(Resouce):
    """DNS zone endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.records = Records(client)

    def display(
        self,
        zone: str,
        *,
        skel: bool = False,
        records: bool = False,
        records_description: bool = False,
        idn: bool = False,
        label: bool = False,
    ) -> DNSZone:
        """Get information for one zone."""
        url = f"/2/zones/{zone}"
        with_values = _build_with_values(
            skel=skel,
            records=records,
            records_description=records_description,
            idn=idn,
            label=label,
        )
        params = {"with": with_values} if with_values is not None else None
        response = self._client.get(url, params=params)
        return from_dict(DNSZone, _extract_zone_payload(response.json()))

    def update(
        self,
        zone: str,
        zone_skel: str,
        *,
        skel: bool = False,
        records: bool = False,
        records_description: bool = False,
        idn: bool = False,
    ) -> DNSZone:
        """Update a given zone."""
        url = f"/2/zones/{zone}"
        with_values = _build_with_values(
            skel=skel,
            records=records,
            records_description=records_description,
            idn=idn,
        )
        params = {"with": with_values} if with_values is not None else None
        response = self._client.put(url, json={"skel": zone_skel}, params=params)
        return from_dict(DNSZone, _extract_zone_payload(response.json()))

    def store(
        self,
        zone: str,
        *,
        zone_skel: str | None = None,
        skel: bool = False,
        records: bool = False,
        records_description: bool = False,
        idn: bool = False,
    ) -> DNSZone:
        """Create a zone."""
        url = f"/2/zones/{zone}"
        with_values = _build_with_values(
            skel=skel,
            records=records,
            records_description=records_description,
            idn=idn,
        )
        params = {"with": with_values} if with_values is not None else None
        payload = {"skel": zone_skel} if zone_skel is not None else None
        response = self._client.post(url, json=payload, params=params)
        return from_dict(DNSZone, _extract_zone_payload(response.json()))

    def delete(self, zone: str) -> bool:
        """Delete a given zone."""
        url = f"/2/zones/{zone}"
        response = self._client.delete(url)
        return bool(response.json()["data"])

    def exists(self, zone: str) -> bool:
        """Check whether one zone exists."""
        url = f"/2/zones/{zone}/exists"
        response = self._client.get(url)
        return bool(response.json()["data"])


class AsyncZone(AsyncResource):
    """Async DNS zone endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.records = AsyncRecords(client)

    async def display(
        self,
        zone: str,
        *,
        skel: bool = False,
        records: bool = False,
        records_description: bool = False,
        idn: bool = False,
        label: bool = False,
    ) -> DNSZone:
        """Get information for one zone."""
        url = f"/2/zones/{zone}"
        with_values = _build_with_values(
            skel=skel,
            records=records,
            records_description=records_description,
            idn=idn,
            label=label,
        )
        params = {"with": with_values} if with_values is not None else None
        response = await self._client.get(url, params=params)
        return from_dict(DNSZone, _extract_zone_payload(response.json()))

    async def update(
        self,
        zone: str,
        zone_skel: str,
        *,
        skel: bool = False,
        records: bool = False,
        records_description: bool = False,
        idn: bool = False,
    ) -> DNSZone:
        """Update a given zone."""
        url = f"/2/zones/{zone}"
        with_values = _build_with_values(
            skel=skel,
            records=records,
            records_description=records_description,
            idn=idn,
        )
        params = {"with": with_values} if with_values is not None else None
        response = await self._client.put(url, json={"skel": zone_skel}, params=params)
        return from_dict(DNSZone, _extract_zone_payload(response.json()))

    async def store(
        self,
        zone: str,
        *,
        zone_skel: str | None = None,
        skel: bool = False,
        records: bool = False,
        records_description: bool = False,
        idn: bool = False,
    ) -> DNSZone:
        """Create a zone."""
        url = f"/2/zones/{zone}"
        with_values = _build_with_values(
            skel=skel,
            records=records,
            records_description=records_description,
            idn=idn,
        )
        params = {"with": with_values} if with_values is not None else None
        payload = {"skel": zone_skel} if zone_skel is not None else None
        response = await self._client.post(url, json=payload, params=params)
        return from_dict(DNSZone, _extract_zone_payload(response.json()))

    async def delete(self, zone: str) -> bool:
        """Delete a given zone."""
        url = f"/2/zones/{zone}"
        response = await self._client.delete(url)
        return bool(response.json()["data"])

    async def exists(self, zone: str) -> bool:
        """Check whether one zone exists."""
        url = f"/2/zones/{zone}/exists"
        response = await self._client.get(url)
        return bool(response.json()["data"])


__all__ = [
    "Zone",
    "AsyncZone",
    "Records",
    "AsyncRecords",
]
