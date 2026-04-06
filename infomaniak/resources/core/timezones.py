from __future__ import annotations

from typing import Literal
from infomaniak.utils import parse, plist, query_params
from infomaniak.models import Timezone
from infomaniak.resource import Resouce, AsyncResource


class Timezones(Resouce):
    """Core timezones endpoints."""

    def list(
        self,
        *,
        search: str | None = None,
        return_: Literal["total"] | None = None,
        limit: int | None = None,
        skip: int | None = None,
        page: int | None = None,
        items: int | None = None,
        order_by: str | None = None,
        order: Literal["asc", "desc"] | None = None,
        order_for: dict[str, Literal["asc", "desc"]] | None = None,
    ) -> plist[Timezone]:
        """
        Retrieve all available timezones.

        Args:
            search: Optional search string used to filter timezone names.
            return_: Optional return mode. Use ``"total"`` to only fetch the total count.
            limit: Optional limit for offset-based pagination.
            skip: Optional offset for offset-based pagination.
            page: Optional page number for paginated responses.
            items: Optional number of items returned per page.
            order_by: Optional field used for sorting.
            order: Optional default sort order.
            order_for: Optional per-field sort order mapping.

        Returns:
            plist[Timezone]: The list of timezones and pagination metadata.
        """
        response = self._client.get(
            "/1/timezones",
            params=query_params(
                search=search,
                limit=limit,
                skip=skip,
                page=page,
                items=items,
                order_by=order_by,
                order=order,
                order_for=order_for,
                **{"return": return_},
            ),
        )
        payload = response.json()
        return plist(
            [parse(Timezone, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    def display(self, timezone_id: int) -> Timezone:
        """
        Retrieve information for a single timezone.

        Args:
            timezone_id: The unique identifier (ID) of the timezone.

        Returns:
            Timezone: The requested timezone.
        """
        response = self._client.get(f"/1/timezones/{timezone_id}")
        return parse(Timezone, response.json()["data"])


class AsyncTimezones(AsyncResource):
    """Async core timezones endpoints."""

    async def list(
        self,
        *,
        search: str | None = None,
        return_: Literal["total"] | None = None,
        limit: int | None = None,
        skip: int | None = None,
        page: int | None = None,
        items: int | None = None,
        order_by: str | None = None,
        order: Literal["asc", "desc"] | None = None,
        order_for: dict[str, Literal["asc", "desc"]] | None = None,
    ) -> plist[Timezone]:
        """
        Retrieve all available timezones.

        Args:
            search: Optional search string used to filter timezone names.
            return_: Optional return mode. Use ``"total"`` to only fetch the total count.
            limit: Optional limit for offset-based pagination.
            skip: Optional offset for offset-based pagination.
            page: Optional page number for paginated responses.
            items: Optional number of items returned per page.
            order_by: Optional field used for sorting.
            order: Optional default sort order.
            order_for: Optional per-field sort order mapping.

        Returns:
            plist[Timezone]: The list of timezones and pagination metadata.
        """
        response = await self._client.get(
            "/1/timezones",
            params=query_params(
                search=search,
                limit=limit,
                skip=skip,
                page=page,
                items=items,
                order_by=order_by,
                order=order,
                order_for=order_for,
                **{"return": return_},
            ),
        )
        payload = response.json()
        return plist(
            [parse(Timezone, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    async def display(self, timezone_id: int) -> Timezone:
        """
        Retrieve information for a single timezone.

        Args:
            timezone_id: The unique identifier (ID) of the timezone.

        Returns:
            Timezone: The requested timezone.
        """
        response = await self._client.get(f"/1/timezones/{timezone_id}")
        return parse(Timezone, response.json()["data"])
