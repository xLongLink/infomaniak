from __future__ import annotations

from dacite import from_dict

from infomaniak.models.dns.zone import DNSZone
from infomaniak.resource import AsyncResource, Resouce

from .records import AsyncRecords, Records


def _build_with_values(
    *,
    skel: bool,
    records: bool,
    records_description: bool,
    idn: bool,
    label: bool = False,
) -> str | None:
    with_values: list[str] = []
    if skel:
        with_values.append("skel")
    if records:
        with_values.append("records")
    if records_description:
        with_values.append("records_description")
    if idn:
        with_values.append("idn")
    if label:
        with_values.append("label")
    return ",".join(with_values) if with_values else None


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
        return from_dict(DNSZone, response.json()["data"])

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
        return from_dict(DNSZone, response.json()["data"])

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
        return from_dict(DNSZone, response.json()["data"])

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
        return from_dict(DNSZone, response.json()["data"])

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
        return from_dict(DNSZone, response.json()["data"])

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
        return from_dict(DNSZone, response.json()["data"])

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
