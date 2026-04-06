from __future__ import annotations

from typing import Any
from infomaniak.resource import Resouce, AsyncResource


class Tasks(Resouce):
    """Core tasks endpoints."""

    def list(
        self,
        *,
        page: int | None = None,
        items: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        List tasks from the core API.

        Args:
            page: Optional page number for paginated responses.
            items: Optional number of tasks to return per page.

        Returns:
            list[dict[str, Any]]: The list of tasks returned by the API.
        """
        params: dict[str, int] = {}
        if page is not None:
            params["page"] = page
        if items is not None:
            params["items"] = items

        response = self._client.get("/1/tasks", params=params or None)
        return response.json()["data"]

    def display(self, task_id: int) -> dict[str, Any]:
        """
        Display one task from the core API.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            dict[str, Any]: The task payload returned by the API.
        """
        response = self._client.get(f"/1/tasks/{task_id}")
        return response.json()["data"]


class AsyncTasks(AsyncResource):
    """Async core tasks endpoints."""

    async def list(
        self,
        *,
        page: int | None = None,
        items: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        List tasks from the core API.

        Args:
            page: Optional page number for paginated responses.
            items: Optional number of tasks to return per page.

        Returns:
            list[dict[str, Any]]: The list of tasks returned by the API.
        """
        params: dict[str, int] = {}
        if page is not None:
            params["page"] = page
        if items is not None:
            params["items"] = items

        response = await self._client.get("/1/tasks", params=params or None)
        return response.json()["data"]

    async def display(self, task_id: int) -> dict[str, Any]:
        """
        Display one task from the core API.

        Args:
            task_id: The unique identifier of the task.

        Returns:
            dict[str, Any]: The task payload returned by the API.
        """
        response = await self._client.get(f"/1/tasks/{task_id}")
        return response.json()["data"]
