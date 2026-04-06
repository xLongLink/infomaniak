from __future__ import annotations

from typing import Any
from infomaniak.resource import Resouce, AsyncResource


class Tasks(Resouce):
    """Tasks endpoints."""

    def list(
        self,
        *,
        page: int | None = None,
        items: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        List asynchronous tasks.

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

        response = self._client.get("/1/async/tasks", params=params or None)
        return response.json()["data"]

    def get(self, task_uuid: str) -> dict[str, Any]:
        """
        Get one asynchronous task.

        Args:
            task_uuid: The unique identifier of the asynchronous task.

        Returns:
            dict[str, Any]: The task payload returned by the API.
        """
        response = self._client.get(f"/1/async/tasks/{task_uuid}")
        return response.json()["data"]


class AsyncTasks(AsyncResource):
    """Async tasks endpoints."""

    async def list(
        self,
        *,
        page: int | None = None,
        items: int | None = None,
    ) -> list[dict[str, Any]]:
        """
        List asynchronous tasks.

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

        response = await self._client.get("/1/async/tasks", params=params or None)
        return response.json()["data"]

    async def get(self, task_uuid: str) -> dict[str, Any]:
        """
        Get one asynchronous task.

        Args:
            task_uuid: The unique identifier of the asynchronous task.

        Returns:
            dict[str, Any]: The task payload returned by the API.
        """
        response = await self._client.get(f"/1/async/tasks/{task_uuid}")
        return response.json()["data"]
