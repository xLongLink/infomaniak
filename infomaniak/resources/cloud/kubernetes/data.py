from __future__ import annotations

from typing import Any
from infomaniak.utils import plist, query_params
from infomaniak.resource import Resouce, AsyncResource


class Data(Resouce):
    """Cloud Kubernetes reference data resources."""

    def list(self) -> dict[str, list[Any]]:
        """
        List available Kubernetes reference datasets.

        Returns:
            dict[str, list[Any]]: A dictionary containing ``packs``, ``versions``, and ``regions``.
        """
        return {
            "packs": self.packs(),
            "versions": self.versions(),
            "regions": self.regions(),
        }

    def packs(self) -> list[dict[str, Any]]:
        """
        List all Kubernetes Service packs for the current client.

        Returns:
            list[dict[str, Any]]: The list of Kubernetes Service packs.
        """
        response = self._client.get("/1/public_clouds/kaas/packs")
        return response.json()["data"]

    def versions(self) -> list[str]:
        """
        List all possible Kubernetes Service versions.

        Returns:
            list[str]: The list of supported Kubernetes versions.
        """
        response = self._client.get("/1/public_clouds/kaas/versions")
        return response.json()["data"]

    def regions(self) -> list[str]:
        """
        List all possible Kubernetes Service regions.

        Returns:
            list[str]: The list of supported Kubernetes regions.
        """
        response = self._client.get("/1/public_clouds/kaas/regions")
        return response.json()["data"]

    def reagions(self) -> list[str]:
        """
        Compatibility alias for :meth:`regions`.

        Returns:
            list[str]: The list of supported Kubernetes regions.
        """
        return self.regions()

    def zones(self, region: str) -> list[str]:
        """
        List all possible Kubernetes Service availability zones for a region.

        Args:
            region: The Public Cloud region (for example ``dc3-a``).

        Returns:
            list[str]: The list of availability zones for the provided region.
        """
        response = self._client.get(
            "/1/public_clouds/kaas/availability_zones",
            params={"region": region},
        )
        return response.json()["data"]

    def flavors(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        *,
        region: str | None = None,
        filter_: dict[str, Any] | None = None,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[dict[str, Any]]:
        """
        List Kubernetes Service flavors for a Public Cloud project.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            region: Optional Public Cloud region (for example ``dc3-a``).
            filter_: Optional API filters.
            page: Optional page number for page-based pagination.
            items: Optional number of items per page for page-based pagination.

        Returns:
            plist[dict[str, Any]]: The list of Kubernetes Service flavors and pagination metadata.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/flavors"
        )
        params = query_params(region=region, filter=filter_, page=page, items=items)
        response = self._client.get(url, params=params)
        payload = response.json()

        return plist(
            payload["data"],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    def flavor(self, public_cloud_id: int, public_cloud_project_id: int, **kwargs: Any) -> plist[dict[str, Any]]:
        """
        Compatibility alias for :meth:`flavors`.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            **kwargs: Forwarded keyword arguments for :meth:`flavors`.

        Returns:
            plist[dict[str, Any]]: The list of Kubernetes Service flavors and pagination metadata.
        """
        return self.flavors(public_cloud_id, public_cloud_project_id, **kwargs)

    def flavor_filters(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        region: str,
    ) -> dict[str, Any]:
        """
        List available filters for Kubernetes Service flavors.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            region: The Public Cloud region (for example ``dc3-a``).

        Returns:
            dict[str, Any]: The available flavor filter values.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/flavors/filters"
        )
        response = self._client.get(url, params={"region": region})
        return response.json()["data"]


class AsyncData(AsyncResource):
    """Async cloud Kubernetes reference data resources."""

    async def list(self) -> dict[str, list[Any]]:
        """
        List available Kubernetes reference datasets.

        Returns:
            dict[str, list[Any]]: A dictionary containing ``packs``, ``versions``, and ``regions``.
        """
        return {
            "packs": await self.packs(),
            "versions": await self.versions(),
            "regions": await self.regions(),
        }

    async def packs(self) -> list[dict[str, Any]]:
        """
        List all Kubernetes Service packs for the current client.

        Returns:
            list[dict[str, Any]]: The list of Kubernetes Service packs.
        """
        response = await self._client.get("/1/public_clouds/kaas/packs")
        return response.json()["data"]

    async def versions(self) -> list[str]:
        """
        List all possible Kubernetes Service versions.

        Returns:
            list[str]: The list of supported Kubernetes versions.
        """
        response = await self._client.get("/1/public_clouds/kaas/versions")
        return response.json()["data"]

    async def regions(self) -> list[str]:
        """
        List all possible Kubernetes Service regions.

        Returns:
            list[str]: The list of supported Kubernetes regions.
        """
        response = await self._client.get("/1/public_clouds/kaas/regions")
        return response.json()["data"]

    async def reagions(self) -> list[str]:
        """
        Compatibility alias for :meth:`regions`.

        Returns:
            list[str]: The list of supported Kubernetes regions.
        """
        return await self.regions()

    async def zones(self, region: str) -> list[str]:
        """
        List all possible Kubernetes Service availability zones for a region.

        Args:
            region: The Public Cloud region (for example ``dc3-a``).

        Returns:
            list[str]: The list of availability zones for the provided region.
        """
        response = await self._client.get(
            "/1/public_clouds/kaas/availability_zones",
            params={"region": region},
        )
        return response.json()["data"]

    async def flavors(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        *,
        region: str | None = None,
        filter_: dict[str, Any] | None = None,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[dict[str, Any]]:
        """
        List Kubernetes Service flavors for a Public Cloud project.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            region: Optional Public Cloud region (for example ``dc3-a``).
            filter_: Optional API filters.
            page: Optional page number for page-based pagination.
            items: Optional number of items per page for page-based pagination.

        Returns:
            plist[dict[str, Any]]: The list of Kubernetes Service flavors and pagination metadata.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/flavors"
        )
        params = query_params(region=region, filter=filter_, page=page, items=items)
        response = await self._client.get(url, params=params)
        payload = response.json()

        return plist(
            payload["data"],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    async def flavor(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        **kwargs: Any,
    ) -> plist[dict[str, Any]]:
        """
        Compatibility alias for :meth:`flavors`.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            **kwargs: Forwarded keyword arguments for :meth:`flavors`.

        Returns:
            plist[dict[str, Any]]: The list of Kubernetes Service flavors and pagination metadata.
        """
        return await self.flavors(public_cloud_id, public_cloud_project_id, **kwargs)

    async def flavor_filters(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        region: str,
    ) -> dict[str, Any]:
        """
        List available filters for Kubernetes Service flavors.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            region: The Public Cloud region (for example ``dc3-a``).

        Returns:
            dict[str, Any]: The available flavor filter values.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/flavors/filters"
        )
        response = await self._client.get(url, params={"region": region})
        return response.json()["data"]
