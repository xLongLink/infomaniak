from __future__ import annotations

from typing import Literal
from .order import Order, AsyncOrder
from .dnssec import DNSSEC, AsyncDNSSEC
from .nameservers import Nameservers, AsyncNameservers
from infomaniak.utils import parse, plist
from infomaniak.resource import Resouce, AsyncResource
from infomaniak.models.domain import Domain as DomainModel


class Domain(Resouce):
    """DNS domain endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.dnssec = DNSSEC(client)
        self.nameservers = Nameservers(client)
        self.order = Order(client)

    def list(
        self,
        *,
        account_id: int | None = None,
        expires_after: int | None = None,
        expires_before: int | None = None,
        order_by: Literal["expiration", "name"] | None = None,
        order_dir: Literal["asc", "desc"] | None = None,
        search: str | None = None,
        tld: str | None = None,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[DomainModel]:
        """
        List domains from `GET /2/domains/domains`.

        Args:
            account_id: Filter domains by account ID.
            expires_after: Filter domains expiring after the provided UNIX timestamp.
            expires_before: Filter domains expiring before the provided UNIX timestamp.
            order_by: Field used to sort results.
            order_dir: Sorting direction.
            search: Free-text search string for domains.
            tld: Filter domains by TLD.
            page: Page number when requesting paginated results.
            items: Number of items per page.

        Returns:
            plist[DomainModel]: The list of domains with pagination metadata.
        """
        params: dict[str, str | int] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if expires_after is not None:
            params["expires_after"] = expires_after
        if expires_before is not None:
            params["expires_before"] = expires_before
        if order_by is not None:
            params["order_by"] = order_by
        if order_dir is not None:
            params["order_dir"] = order_dir
        if search is not None:
            params["search"] = search
        if tld is not None:
            params["tld"] = tld
        if page is not None:
            params["page"] = page
        if items is not None:
            params["items"] = items

        response = self._client.get("/2/domains/domains", params=params or None)
        payload = response.json()
        return plist(
            [parse(DomainModel, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    def show(self, domain: str) -> DomainModel:
        """
        Show one domain from `GET /2/domains/domains/{domain}`.

        Args:
            domain: Domain name to retrieve.

        Returns:
            DomainModel: The matching domain details.
        """
        response = self._client.get(f"/2/domains/domains/{domain}")
        return parse(DomainModel, response.json()["data"])

    def display(self, domain: str) -> DomainModel:
        """
        Display one domain.

        Args:
            domain: Domain name to retrieve.

        Returns:
            DomainModel: The matching domain details.
        """
        return self.show(domain)


class AsyncDomain(AsyncResource):
    """Async DNS domain endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.dnssec = AsyncDNSSEC(client)
        self.nameservers = AsyncNameservers(client)
        self.order = AsyncOrder(client)

    async def list(
        self,
        *,
        account_id: int | None = None,
        expires_after: int | None = None,
        expires_before: int | None = None,
        order_by: Literal["expiration", "name"] | None = None,
        order_dir: Literal["asc", "desc"] | None = None,
        search: str | None = None,
        tld: str | None = None,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[DomainModel]:
        """
        List domains from `GET /2/domains/domains`.

        Args:
            account_id: Filter domains by account ID.
            expires_after: Filter domains expiring after the provided UNIX timestamp.
            expires_before: Filter domains expiring before the provided UNIX timestamp.
            order_by: Field used to sort results.
            order_dir: Sorting direction.
            search: Free-text search string for domains.
            tld: Filter domains by TLD.
            page: Page number when requesting paginated results.
            items: Number of items per page.

        Returns:
            plist[DomainModel]: The list of domains with pagination metadata.
        """
        params: dict[str, str | int] = {}
        if account_id is not None:
            params["account_id"] = account_id
        if expires_after is not None:
            params["expires_after"] = expires_after
        if expires_before is not None:
            params["expires_before"] = expires_before
        if order_by is not None:
            params["order_by"] = order_by
        if order_dir is not None:
            params["order_dir"] = order_dir
        if search is not None:
            params["search"] = search
        if tld is not None:
            params["tld"] = tld
        if page is not None:
            params["page"] = page
        if items is not None:
            params["items"] = items

        response = await self._client.get("/2/domains/domains", params=params or None)
        payload = response.json()
        return plist(
            [parse(DomainModel, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    async def show(self, domain: str) -> DomainModel:
        """
        Show one domain from `GET /2/domains/domains/{domain}`.

        Args:
            domain: Domain name to retrieve.

        Returns:
            DomainModel: The matching domain details.
        """
        response = await self._client.get(f"/2/domains/domains/{domain}")
        return parse(DomainModel, response.json()["data"])

    async def display(self, domain: str) -> DomainModel:
        """
        Display one domain.

        Args:
            domain: Domain name to retrieve.

        Returns:
            DomainModel: The matching domain details.
        """
        return await self.show(domain)
