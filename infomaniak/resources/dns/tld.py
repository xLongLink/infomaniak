from dacite import from_dict

from infomaniak.models.dns.tld import Tld
from infomaniak.resource import AsyncResource, Resouce
from infomaniak.utils import _with


class TLD(Resouce):
    """DNS TLD endpoints."""

    def list(
        self,
        *,
        length: bool = False,
        periods: bool = False,
        group: bool = False,
        transfer_method: bool = False,
        is_idn: bool = False,
        support: bool = False,
        time: bool = False,
        groups: list[int] | None = None,
    ) -> list[Tld]:
        """List all available TLDs."""
        url = "/2/tld"
        params: dict[str, str | list[int]] = {}
        with_values = _with(
            length=length,
            periods=periods,
            groups=group,
            transfer_method=transfer_method,
            is_idn=is_idn,
            support=support,
            time=time,
        )
        if with_values is not None:
            params["with"] = with_values
        if groups is not None:
            params["groups"] = groups
        response = self._client.get(url, params=params or None)
        return [from_dict(Tld, item) for item in response.json()["data"]]

    def show(
        self,
        tld: str,
        *,
        length: bool = False,
        periods: bool = False,
        group: bool = False,
        transfer_method: bool = False,
        is_idn: bool = False,
        support: bool = False,
        time: bool = False,
    ) -> Tld:
        """Show one TLD."""
        url = f"/2/tld/{tld}"
        with_values = _with(
            length=length,
            periods=periods,
            groups=group,
            transfer_method=transfer_method,
            is_idn=is_idn,
            support=support,
            time=time,
        )
        params = {"with": with_values} if with_values is not None else None
        response = self._client.get(url, params=params)
        return from_dict(Tld, response.json()["data"])


class AsyncTLD(AsyncResource):
    """Async DNS TLD endpoints."""

    async def list(
        self,
        *,
        length: bool = False,
        periods: bool = False,
        group: bool = False,
        transfer_method: bool = False,
        is_idn: bool = False,
        support: bool = False,
        time: bool = False,
        groups: list[int] | None = None,
    ) -> list[Tld]:
        """List all available TLDs."""
        url = "/2/tld"
        params: dict[str, str | list[int]] = {}
        with_values = _with(
            length=length,
            periods=periods,
            groups=group,
            transfer_method=transfer_method,
            is_idn=is_idn,
            support=support,
            time=time,
        )
        if with_values is not None:
            params["with"] = with_values
        if groups is not None:
            params["groups"] = groups
        response = await self._client.get(url, params=params or None)
        return [from_dict(Tld, item) for item in response.json()["data"]]

    async def show(
        self,
        tld: str,
        *,
        length: bool = False,
        periods: bool = False,
        group: bool = False,
        transfer_method: bool = False,
        is_idn: bool = False,
        support: bool = False,
        time: bool = False,
    ) -> Tld:
        """Show one TLD."""
        url = f"/2/tld/{tld}"
        with_values = _with(
            length=length,
            periods=periods,
            groups=group,
            transfer_method=transfer_method,
            is_idn=is_idn,
            support=support,
            time=time,
        )
        params = {"with": with_values} if with_values is not None else None
        response = await self._client.get(url, params=params)
        return from_dict(Tld, response.json()["data"])
