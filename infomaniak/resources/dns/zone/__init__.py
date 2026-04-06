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
    description: bool,
    idn: bool,
    label: bool = False,
) -> str | None:
    """
    Build the `with` query parameter value for DNS zone endpoints.

    Args:
        skel: Whether to include the raw zone skeleton in the response.
        records: Whether to include DNS records in the response.
        description: Whether to include record descriptions in the response.
        idn: Whether to include IDN values in the response.
        label: Whether to include the zone label in the response.

    Returns:
        str | None: A comma-separated `with` value, or `None` when empty.
    """
    return _with(
        skel=skel,
        records=records,
        description=description,
        idn=idn,
        label=label,
    )


def _extract_zone_payload(
    payload: dict[str, Any],
) -> dict[str, Any]:
    """
    Normalize DNS zone responses that may be wrapped or returned directly.

    Args:
        payload: The raw API response payload.

    Returns:
        dict[str, Any]: The normalized DNS zone payload.
    """
    data = payload.get("data")
    if isinstance(data, dict):
        return data
    return payload


def _extract_zone_exists_payload(
    payload: dict[str, Any],
) -> bool:
    """
    Normalize DNS zone existence responses into a boolean.

    Args:
        payload: The raw API response payload.

    Returns:
        bool: `True` when the zone exists, otherwise `False`.
    """
    data = payload.get("data")
    if isinstance(data, bool):
        return data
    if data is not None:
        return bool(data)

    error = payload.get("error")
    if isinstance(error, dict) and error.get("code") == "zone_does_not_exists":
        return False

    raise KeyError("Expected 'data' in DNS zone exists response payload.")


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
        description: bool = False,
        idn: bool = False,
        label: bool = False,
    ) -> DNSZone:
        """
        Get information for one DNS zone.

        Args:
            zone: Fully qualified domain name of the DNS zone.
            skel: Whether to include the raw zone skeleton in the response.
            records: Whether to include DNS records in the response.
            description: Whether to include DNS record descriptions in the response.
            idn: Whether to include IDN values in the response.
            label: Whether to include the zone label in the response.

        Returns:
            DNSZone: The DNS zone details returned by the API.
        """
        url = f"/2/zones/{zone}"
        with_values = _build_with_values(
            skel=skel,
            records=records,
            description=description,
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
        description: bool = False,
        idn: bool = False,
    ) -> DNSZone:
        """
        Update a given DNS zone.

        Args:
            zone: Fully qualified domain name of the DNS zone.
            zone_skel: New zone skeleton content to apply.
            skel: Whether to include the updated raw zone skeleton in the response.
            records: Whether to include updated DNS records in the response.
            description: Whether to include updated DNS record descriptions.
            idn: Whether to include IDN values in the response.

        Returns:
            DNSZone: The updated DNS zone returned by the API.
        """
        url = f"/2/zones/{zone}"
        with_values = _build_with_values(
            skel=skel,
            records=records,
            description=description,
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
        description: bool = False,
        idn: bool = False,
    ) -> DNSZone:
        """
        Create a DNS zone.

        Args:
            zone: Fully qualified domain name of the DNS zone to create.
            zone_skel: Initial zone skeleton content, or `None` for defaults.
            skel: Whether to include the created raw zone skeleton in the response.
            records: Whether to include DNS records in the response.
            description: Whether to include DNS record descriptions in the response.
            idn: Whether to include IDN values in the response.

        Returns:
            DNSZone: The created DNS zone returned by the API.
        """
        url = f"/2/zones/{zone}"
        with_values = _build_with_values(
            skel=skel,
            records=records,
            description=description,
            idn=idn,
        )
        params = {"with": with_values} if with_values is not None else None
        payload = {"skel": zone_skel} if zone_skel is not None else None
        response = self._client.post(url, json=payload, params=params)
        return from_dict(DNSZone, _extract_zone_payload(response.json()))

    def delete(self, zone: str) -> bool:
        """
        Delete a given DNS zone.

        Args:
            zone: Fully qualified domain name of the DNS zone to delete.

        Returns:
            bool: `True` when deletion succeeded, otherwise `False`.
        """
        url = f"/2/zones/{zone}"
        response = self._client.delete(url)
        return bool(response.json()["data"])

    def exists(self, zone: str) -> bool:
        """
        Check whether one DNS zone exists.

        Args:
            zone: Fully qualified domain name of the DNS zone to check.

        Returns:
            bool: `True` when the zone exists, otherwise `False`.
        """
        url = f"/2/zones/{zone}/exists"
        response = self._client.get(url)
        return _extract_zone_exists_payload(response.json())


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
        description: bool = False,
        idn: bool = False,
        label: bool = False,
    ) -> DNSZone:
        """
        Get information for one DNS zone.

        Args:
            zone: Fully qualified domain name of the DNS zone.
            skel: Whether to include the raw zone skeleton in the response.
            records: Whether to include DNS records in the response.
            description: Whether to include DNS record descriptions in the response.
            idn: Whether to include IDN values in the response.
            label: Whether to include the zone label in the response.

        Returns:
            DNSZone: The DNS zone details returned by the API.
        """
        url = f"/2/zones/{zone}"
        with_values = _build_with_values(
            skel=skel,
            records=records,
            description=description,
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
        description: bool = False,
        idn: bool = False,
    ) -> DNSZone:
        """
        Update a given DNS zone.

        Args:
            zone: Fully qualified domain name of the DNS zone.
            zone_skel: New zone skeleton content to apply.
            skel: Whether to include the updated raw zone skeleton in the response.
            records: Whether to include updated DNS records in the response.
            description: Whether to include updated DNS record descriptions.
            idn: Whether to include IDN values in the response.

        Returns:
            DNSZone: The updated DNS zone returned by the API.
        """
        url = f"/2/zones/{zone}"
        with_values = _build_with_values(
            skel=skel,
            records=records,
            description=description,
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
        description: bool = False,
        idn: bool = False,
    ) -> DNSZone:
        """
        Create a DNS zone.

        Args:
            zone: Fully qualified domain name of the DNS zone to create.
            zone_skel: Initial zone skeleton content, or `None` for defaults.
            skel: Whether to include the created raw zone skeleton in the response.
            records: Whether to include DNS records in the response.
            description: Whether to include DNS record descriptions in the response.
            idn: Whether to include IDN values in the response.

        Returns:
            DNSZone: The created DNS zone returned by the API.
        """
        url = f"/2/zones/{zone}"
        with_values = _build_with_values(
            skel=skel,
            records=records,
            description=description,
            idn=idn,
        )
        params = {"with": with_values} if with_values is not None else None
        payload = {"skel": zone_skel} if zone_skel is not None else None
        response = await self._client.post(url, json=payload, params=params)
        return from_dict(DNSZone, _extract_zone_payload(response.json()))

    async def delete(self, zone: str) -> bool:
        """
        Delete a given DNS zone.

        Args:
            zone: Fully qualified domain name of the DNS zone to delete.

        Returns:
            bool: `True` when deletion succeeded, otherwise `False`.
        """
        url = f"/2/zones/{zone}"
        response = await self._client.delete(url)
        return bool(response.json()["data"])

    async def exists(self, zone: str) -> bool:
        """
        Check whether one DNS zone exists.

        Args:
            zone: Fully qualified domain name of the DNS zone to check.

        Returns:
            bool: `True` when the zone exists, otherwise `False`.
        """
        url = f"/2/zones/{zone}/exists"
        response = await self._client.get(url)
        return _extract_zone_exists_payload(response.json())
