from __future__ import annotations

from typing import Literal
from infomaniak.utils import parse, plist, query_params
from infomaniak.resource import Resouce, AsyncResource
from infomaniak.models.chk import ChkQuota, ChkShortUrl, ChkShortUrlResponse

ChkOrderBy = Literal["code", "url", "created_at", "expiration_date"]
ChkOrderDirection = Literal["ASC", "DESC"]


class Chk(Resouce):
    """CHK URL shortener endpoints."""

    def create(
        self,
        url: str,
        *,
        expiration_date: int | None = None,
    ) -> ChkShortUrlResponse:
        """
        Create a short URL.

        Args:
            url: The URL to shorten.
            expiration_date: Optional Unix timestamp when the short URL expires.

        Returns:
            ChkShortUrlResponse: The created short URL payload.
        """
        payload: dict[str, str | int] = {"url": url}
        if expiration_date is not None:
            payload["expiration_date"] = expiration_date

        response = self._client.post("/1/url-shortener", json=payload)
        return parse(ChkShortUrlResponse, response.json())

    def list(
        self,
        *,
        order_by: ChkOrderBy | None = None,
        order_direction: ChkOrderDirection | None = None,
        search: str | None = None,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[ChkShortUrl]:
        """
        List short URLs.

        Args:
            order_by: Optional ordering field.
            order_direction: Optional ordering direction.
            search: Optional search string used to filter URL entries.
            page: Optional page number for paginated responses.
            items: Optional number of items to return per page.

        Returns:
            plist[ChkShortUrl]: The list of short URLs and pagination metadata.
        """
        response = self._client.get(
            "/2/url-shortener",
            params=query_params(
                order_by=order_by,
                order_direction=order_direction,
                search=search,
                page=page,
                per_page=items,
            ),
        )
        payload = response.json()
        return plist(
            [parse(ChkShortUrl, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    def update(
        self,
        short_url_code: str,
        *,
        expiration_date: int | None = None,
    ) -> ChkShortUrlResponse:
        """
        Update a short URL expiration date.

        Args:
            short_url_code: The short URL code to update.
            expiration_date: Optional Unix timestamp when the short URL expires.

        Returns:
            ChkShortUrlResponse: The updated short URL payload.
        """
        payload: dict[str, int] = {}
        if expiration_date is not None:
            payload["expiration_date"] = expiration_date

        response = self._client.put(
            f"/1/url-shortener/{short_url_code}",
            json=payload,
        )
        return parse(ChkShortUrlResponse, response.json())

    def quota(self) -> ChkQuota:
        """
        Get short URL quota.

        Args:
            None.

        Returns:
            ChkQuota: The current short URL quota and limit.
        """
        response = self._client.get("/2/url-shortener/quota")
        return parse(ChkQuota, response.json()["data"])


class AsyncChk(AsyncResource):
    """Async CHK URL shortener endpoints."""

    async def create(
        self,
        url: str,
        *,
        expiration_date: int | None = None,
    ) -> ChkShortUrlResponse:
        """
        Create a short URL.

        Args:
            url: The URL to shorten.
            expiration_date: Optional Unix timestamp when the short URL expires.

        Returns:
            ChkShortUrlResponse: The created short URL payload.
        """
        payload: dict[str, str | int] = {"url": url}
        if expiration_date is not None:
            payload["expiration_date"] = expiration_date

        response = await self._client.post("/1/url-shortener", json=payload)
        return parse(ChkShortUrlResponse, response.json())

    async def list(
        self,
        *,
        order_by: ChkOrderBy | None = None,
        order_direction: ChkOrderDirection | None = None,
        search: str | None = None,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[ChkShortUrl]:
        """
        List short URLs.

        Args:
            order_by: Optional ordering field.
            order_direction: Optional ordering direction.
            search: Optional search string used to filter URL entries.
            page: Optional page number for paginated responses.
            items: Optional number of items to return per page.

        Returns:
            plist[ChkShortUrl]: The list of short URLs and pagination metadata.
        """
        response = await self._client.get(
            "/2/url-shortener",
            params=query_params(
                order_by=order_by,
                order_direction=order_direction,
                search=search,
                page=page,
                per_page=items,
            ),
        )
        payload = response.json()
        return plist(
            [parse(ChkShortUrl, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    async def update(
        self,
        short_url_code: str,
        *,
        expiration_date: int | None = None,
    ) -> ChkShortUrlResponse:
        """
        Update a short URL expiration date.

        Args:
            short_url_code: The short URL code to update.
            expiration_date: Optional Unix timestamp when the short URL expires.

        Returns:
            ChkShortUrlResponse: The updated short URL payload.
        """
        payload: dict[str, int] = {}
        if expiration_date is not None:
            payload["expiration_date"] = expiration_date

        response = await self._client.put(
            f"/1/url-shortener/{short_url_code}",
            json=payload,
        )
        return parse(ChkShortUrlResponse, response.json())

    async def quota(self) -> ChkQuota:
        """
        Get short URL quota.

        Args:
            None.

        Returns:
            ChkQuota: The current short URL quota and limit.
        """
        response = await self._client.get("/2/url-shortener/quota")
        return parse(ChkQuota, response.json()["data"])
