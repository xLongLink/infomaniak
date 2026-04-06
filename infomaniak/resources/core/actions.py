from __future__ import annotations

from infomaniak.utils import parse, query_params
from infomaniak.models import Action
from infomaniak.resource import Resouce, AsyncResource


class Actions(Resouce):
    """Core actions endpoints."""

    def list(self, *, search: str | None = None) -> list[Action]:
        """
        Retrieve available core actions.

        Args:
            search: Optional search string used to filter action codes.

        Returns:
            list[Action]: The list of available action types.
        """
        response = self._client.get(
            "/1/actions",
            params=query_params(search=search),
        )
        return [parse(Action, item) for item in response.json()["data"]]

    def get(self, action_id: int) -> Action:
        """
        Retrieve one core action by its unique identifier.

        Args:
            action_id: The unique identifier of the action to request.

        Returns:
            Action: The requested action.
        """
        response = self._client.get(f"/1/actions/{action_id}")
        return parse(Action, response.json()["data"])


class AsyncActions(AsyncResource):
    """Async core actions endpoints."""

    async def list(self, *, search: str | None = None) -> list[Action]:
        """
        Retrieve available core actions.

        Args:
            search: Optional search string used to filter action codes.

        Returns:
            list[Action]: The list of available action types.
        """
        response = await self._client.get(
            "/1/actions",
            params=query_params(search=search),
        )
        return [parse(Action, item) for item in response.json()["data"]]

    async def get(self, action_id: int) -> Action:
        """
        Retrieve one core action by its unique identifier.

        Args:
            action_id: The unique identifier of the action to request.

        Returns:
            Action: The requested action.
        """
        response = await self._client.get(f"/1/actions/{action_id}")
        return parse(Action, response.json()["data"])
