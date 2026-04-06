from __future__ import annotations

from typing import Any, Literal
from infomaniak.utils import query_params
from infomaniak.resource import Resouce, AsyncResource

EventType = Literal["internal", "public", "server", "streaming"]
EventStatus = Literal["inprogress", "planned", "reviewed", "terminated"]
Locale = Literal["de", "en", "es", "fr", "it"]


class Events(Resouce):
    """Core events endpoints."""

    def list(
        self,
        *,
        date_from: int | None = None,
        date_to: int | None = None,
        event_type: EventType | None = None,
        is_cyberattack: bool | None = None,
        locale: Locale | None = None,
        show_auto: bool | None = None,
        status: EventStatus | None = None,
        user_id: int | None = None,
        with_trashed: bool | None = None,
        event_types: list[EventType] | None = None,
    ) -> list[dict[str, Any]]:
        """
        Retrieve all opened events.

        Args:
            date_from: Optional Unix timestamp used to filter events starting from this date.
            date_to: Optional Unix timestamp used to filter events until this date.
            event_type: Optional event type filter.
            is_cyberattack: Optional flag to filter cyberattack-related events.
            locale: Optional locale used for localized response fields.
            show_auto: Optional flag to include automatically generated events.
            status: Optional event status filter.
            user_id: Optional user identifier used to filter user-related events.
            with_trashed: Optional flag to include trashed events.
            event_types: Optional list of event types to filter multiple categories.

        Returns:
            list[dict[str, Any]]: The list of events returned by the API.
        """
        response = self._client.get(
            "/2/events",
            params=query_params(
                date_from=date_from,
                date_to=date_to,
                event_type=event_type,
                is_cyberattack=is_cyberattack,
                locale=locale,
                show_auto=show_auto,
                status=status,
                user_id=user_id,
                with_trashed=with_trashed,
                event_types=event_types,
            ),
        )
        return response.json()["data"]

    def display(self, event_id: int) -> dict[str, Any]:
        """
        Retrieve one event by its identifier.

        Args:
            event_id: The unique identifier (ID) of the event to request.

        Returns:
            dict[str, Any]: The event payload returned by the API.
        """
        response = self._client.get(f"/2/events/{event_id}")
        return response.json()["data"]

    def status(self) -> dict[str, Any]:
        """
        Retrieve Public Cloud status information.

        Returns:
            dict[str, Any]: The Public Cloud status payload returned by the API.
        """
        response = self._client.get("/2/events/public-cloud-status")
        return response.json().get("data", {})


class AsyncEvents(AsyncResource):
    """Async core events endpoints."""

    async def list(
        self,
        *,
        date_from: int | None = None,
        date_to: int | None = None,
        event_type: EventType | None = None,
        is_cyberattack: bool | None = None,
        locale: Locale | None = None,
        show_auto: bool | None = None,
        status: EventStatus | None = None,
        user_id: int | None = None,
        with_trashed: bool | None = None,
        event_types: list[EventType] | None = None,
    ) -> list[dict[str, Any]]:
        """
        Retrieve all opened events.

        Args:
            date_from: Optional Unix timestamp used to filter events starting from this date.
            date_to: Optional Unix timestamp used to filter events until this date.
            event_type: Optional event type filter.
            is_cyberattack: Optional flag to filter cyberattack-related events.
            locale: Optional locale used for localized response fields.
            show_auto: Optional flag to include automatically generated events.
            status: Optional event status filter.
            user_id: Optional user identifier used to filter user-related events.
            with_trashed: Optional flag to include trashed events.
            event_types: Optional list of event types to filter multiple categories.

        Returns:
            list[dict[str, Any]]: The list of events returned by the API.
        """
        response = await self._client.get(
            "/2/events",
            params=query_params(
                date_from=date_from,
                date_to=date_to,
                event_type=event_type,
                is_cyberattack=is_cyberattack,
                locale=locale,
                show_auto=show_auto,
                status=status,
                user_id=user_id,
                with_trashed=with_trashed,
                event_types=event_types,
            ),
        )
        return response.json()["data"]

    async def display(self, event_id: int) -> dict[str, Any]:
        """
        Retrieve one event by its identifier.

        Args:
            event_id: The unique identifier (ID) of the event to request.

        Returns:
            dict[str, Any]: The event payload returned by the API.
        """
        response = await self._client.get(f"/2/events/{event_id}")
        return response.json()["data"]

    async def status(self) -> dict[str, Any]:
        """
        Retrieve Public Cloud status information.

        Returns:
            dict[str, Any]: The Public Cloud status payload returned by the API.
        """
        response = await self._client.get("/2/events/public-cloud-status")
        return response.json().get("data", {})
