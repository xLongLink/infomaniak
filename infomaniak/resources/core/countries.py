from __future__ import annotations

from infomaniak.utils import parse, query_params
from infomaniak.models import Country
from infomaniak.resource import Resouce, AsyncResource


class Countries(Resouce):
    """Core countries endpoints."""

    def list(
        self,
        *,
        only_enabled: bool | None = None,
        only_enabled_exception: list[int] | None = None,
        search: str | None = None,
    ) -> list[Country]:
        """
        Retrieve all available countries.

        Args:
            only_enabled: Optional flag to return only enabled countries.
            only_enabled_exception: Optional country IDs to include when
                `only_enabled` is set.
            search: Optional search string used to filter country names.

        Returns:
            list[Country]: The list of countries returned by the API.
        """
        response = self._client.get(
            "/1/countries",
            params=query_params(
                only_enabled=only_enabled,
                only_enabled_exception=only_enabled_exception,
                search=search,
            ),
        )
        return [parse(Country, item) for item in response.json()["data"]]

    def display(self, country_id: int) -> Country:
        """
        Retrieve information for a single country.

        Args:
            country_id: The unique identifier (ID) of the country.

        Returns:
            Country: The requested country.
        """
        response = self._client.get(f"/1/countries/{country_id}")
        return parse(Country, response.json()["data"])


class AsyncCountries(AsyncResource):
    """Async core countries endpoints."""

    async def list(
        self,
        *,
        only_enabled: bool | None = None,
        only_enabled_exception: list[int] | None = None,
        search: str | None = None,
    ) -> list[Country]:
        """
        Retrieve all available countries.

        Args:
            only_enabled: Optional flag to return only enabled countries.
            only_enabled_exception: Optional country IDs to include when
                `only_enabled` is set.
            search: Optional search string used to filter country names.

        Returns:
            list[Country]: The list of countries returned by the API.
        """
        response = await self._client.get(
            "/1/countries",
            params=query_params(
                only_enabled=only_enabled,
                only_enabled_exception=only_enabled_exception,
                search=search,
            ),
        )
        return [parse(Country, item) for item in response.json()["data"]]

    async def display(self, country_id: int) -> Country:
        """
        Retrieve information for a single country.

        Args:
            country_id: The unique identifier (ID) of the country.

        Returns:
            Country: The requested country.
        """
        response = await self._client.get(f"/1/countries/{country_id}")
        return parse(Country, response.json()["data"])
