from __future__ import annotations

from infomaniak.resource import Resouce, AsyncResource


class Ip(Resouce):
    """Cloud Kubernetes API server IP filter resources."""

    def list(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
    ) -> list[str]:
        """
        List all API server IP filters for a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.

        Returns:
            list[str]: The configured list of IP filter CIDRs.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}/ip_filters"
        )
        response = self._client.get(url)
        return response.json()["data"]

    def match(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        ip_filters: list[str],
    ) -> bool:
        """
        Create or replace API server IP filters for a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.
            ip_filters: The whitelist of IP CIDRs to apply.

        Returns:
            bool: True when the update operation reports success, else False.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}/ip_filters"
        )
        response = self._client.put(url, json={"ip_filters": ip_filters})
        return bool(response.json()["data"])

    def remove(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
    ) -> bool:
        """
        Remove all API server IP filters from a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.

        Returns:
            bool: True when the deletion operation reports success, else False.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}/ip_filters"
        )
        response = self._client.delete(url)
        return bool(response.json()["data"])


class AsyncIp(AsyncResource):
    """Async cloud Kubernetes API server IP filter resources."""

    async def list(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
    ) -> list[str]:
        """
        List all API server IP filters for a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.

        Returns:
            list[str]: The configured list of IP filter CIDRs.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}/ip_filters"
        )
        response = await self._client.get(url)
        return response.json()["data"]

    async def match(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        ip_filters: list[str],
    ) -> bool:
        """
        Create or replace API server IP filters for a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.
            ip_filters: The whitelist of IP CIDRs to apply.

        Returns:
            bool: True when the update operation reports success, else False.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}/ip_filters"
        )
        response = await self._client.put(url, json={"ip_filters": ip_filters})
        return bool(response.json()["data"])

    async def remove(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
    ) -> bool:
        """
        Remove all API server IP filters from a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.

        Returns:
            bool: True when the deletion operation reports success, else False.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}/ip_filters"
        )
        response = await self._client.delete(url)
        return bool(response.json()["data"])
