from infomaniak.utils import _with, parse
from infomaniak.resource import Resouce, AsyncResource
from infomaniak.models.dns.tld import Tld


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
        """
        List all available top-level domains.

        Args:
            length: Include allowed domain length constraints when set to ``True``.
            periods: Include domain lifecycle periods when set to ``True``.
            group: Include TLD group metadata when set to ``True``.
            transfer_method: Include transfer method information when set to ``True``.
            is_idn: Include IDN support information when set to ``True``.
            support: Include supported feature information when set to ``True``.
            time: Include registration and transfer timing information when set to ``True``.
            groups: Filter results to the provided group identifiers.

        Returns:
            list[Tld]: The list of top-level domains returned by the API.
        """
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
        return [parse(Tld, item) for item in response.json()["data"]]

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
        """
        Show one top-level domain.

        Args:
            tld: TLD code to retrieve, for example ``ch`` or ``com``.
            length: Include allowed domain length constraints when set to ``True``.
            periods: Include domain lifecycle periods when set to ``True``.
            group: Include TLD group metadata when set to ``True``.
            transfer_method: Include transfer method information when set to ``True``.
            is_idn: Include IDN support information when set to ``True``.
            support: Include supported feature information when set to ``True``.
            time: Include registration and transfer timing information when set to ``True``.

        Returns:
            Tld: The top-level domain details returned by the API.
        """
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
        return parse(Tld, response.json()["data"])


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
        """
        List all available top-level domains.

        Args:
            length: Include allowed domain length constraints when set to ``True``.
            periods: Include domain lifecycle periods when set to ``True``.
            group: Include TLD group metadata when set to ``True``.
            transfer_method: Include transfer method information when set to ``True``.
            is_idn: Include IDN support information when set to ``True``.
            support: Include supported feature information when set to ``True``.
            time: Include registration and transfer timing information when set to ``True``.
            groups: Filter results to the provided group identifiers.

        Returns:
            list[Tld]: The list of top-level domains returned by the API.
        """
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
        return [parse(Tld, item) for item in response.json()["data"]]

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
        """
        Show one top-level domain.

        Args:
            tld: TLD code to retrieve, for example ``ch`` or ``com``.
            length: Include allowed domain length constraints when set to ``True``.
            periods: Include domain lifecycle periods when set to ``True``.
            group: Include TLD group metadata when set to ``True``.
            transfer_method: Include transfer method information when set to ``True``.
            is_idn: Include IDN support information when set to ``True``.
            support: Include supported feature information when set to ``True``.
            time: Include registration and transfer timing information when set to ``True``.

        Returns:
            Tld: The top-level domain details returned by the API.
        """
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
        return parse(Tld, response.json()["data"])
