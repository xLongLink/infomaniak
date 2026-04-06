from __future__ import annotations

from infomaniak.utils import PaginatedList, parse, query_params
from infomaniak.models import Timezone
from infomaniak.resource import Resouce, AsyncResource


class Timezones(Resouce):
    """Core timezones endpoints."""

    def list(
        self,
        *,
        search: str | None = None,
        page: int | None = None,
        per_page: int | None = None,
    ) -> PaginatedList[Timezone]:
        """
        Retrieve all available timezones.

        Args:
            search: Optional search string used to filter timezone names.
            page: Optional page number for paginated responses.
            per_page: Optional number of items returned per page.

        Returns:
            PaginatedList[Timezone]: The list of timezones and pagination metadata.
        """
        response = self._client.get(
            "/1/timezones",
            params=query_params(search=search, page=page, per_page=per_page),
        )
        payload = response.json()
        return PaginatedList(
            [parse(Timezone, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            items=payload.get("total") or 0,
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
        page: int | None = None,
        per_page: int | None = None,
    ) -> PaginatedList[Timezone]:
        """
        Retrieve all available timezones.

        Args:
            search: Optional search string used to filter timezone names.
            page: Optional page number for paginated responses.
            per_page: Optional number of items returned per page.

        Returns:
            PaginatedList[Timezone]: The list of timezones and pagination metadata.
        """
        response = await self._client.get(
            "/1/timezones",
            params=query_params(search=search, page=page, per_page=per_page),
        )
        payload = response.json()
        return PaginatedList(
            [parse(Timezone, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            items=payload.get("total") or 0,
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
