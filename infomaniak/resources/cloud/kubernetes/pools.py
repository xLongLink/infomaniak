from __future__ import annotations

from typing import Any
from infomaniak.utils import plist, query_params
from infomaniak.resource import Resouce, AsyncResource


class Pools(Resouce):
    """Cloud Kubernetes instance pool resources."""

    def list(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        *,
        filter_: dict[str, Any] | None = None,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[dict[str, Any]]:
        """
        List all instance pools for a Kubernetes service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.
            filter_: Optional API filters.
            page: Optional page number for paginated responses.
            items: Optional number of items to return per page.

        Returns:
            plist[dict[str, Any]]: The list of instance pools and pagination metadata.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}/instance_pools"
        )
        params = query_params(filter=filter_, page=page, items=items)

        response = self._client.get(url, params=params)
        payload = response.json()

        return plist(
            payload["data"],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    def create(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        flavor: str,
        minimum_instances: int,
        name: str,
        *,
        availability_zone: str | None = None,
        labels: list[str] | None = None,
        maximum_instances: int | None = None,
        prefix: str | None = None,
    ) -> int:
        """
        Create an instance pool for a Kubernetes service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.
            flavor: The instance pool flavor.
            minimum_instances: The minimum number of instances.
            name: The instance pool name.
            availability_zone: Optional availability zone.
            labels: Optional Kubernetes labels to apply on instances.
            maximum_instances: Optional maximum number of instances.
            prefix: Optional prefix used when naming instances.

        Returns:
            int: The unique identifier of the newly created instance pool.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}/instance_pools"
        )
        payload: dict[str, Any] = {
            "flavor": flavor,
            "minimum_instances": minimum_instances,
            "name": name,
        }
        if availability_zone is not None:
            payload["availability_zone"] = availability_zone
        if labels is not None:
            payload["labels"] = labels
        if maximum_instances is not None:
            payload["maximum_instances"] = maximum_instances
        if prefix is not None:
            payload["prefix"] = prefix

        response = self._client.post(url, json=payload)
        return response.json()["data"]

    def get(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        kaas_worker_pool_id: int,
    ) -> dict[str, Any]:
        """
        Retrieve an instance pool from a Kubernetes service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.
            kaas_worker_pool_id: The unique identifier of the instance pool.

        Returns:
            dict[str, Any]: The instance pool details.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/"
            f"kaas/{kaas_id}/instance_pools/{kaas_worker_pool_id}"
        )
        response = self._client.get(url)
        return response.json()["data"]

    def update(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        kaas_worker_pool_id: int,
        *,
        labels: list[str] | None = None,
        maximum_instances: int | None = None,
        minimum_instances: int | None = None,
        name: str | None = None,
    ) -> bool:
        """
        Update an instance pool for a Kubernetes service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.
            kaas_worker_pool_id: The unique identifier of the instance pool.
            labels: Optional Kubernetes labels to apply on instances.
            maximum_instances: Optional maximum number of instances.
            minimum_instances: Optional minimum number of instances.
            name: Optional instance pool name.

        Returns:
            bool: ``True`` when the update request is accepted, otherwise ``False``.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/"
            f"kaas/{kaas_id}/instance_pools/{kaas_worker_pool_id}"
        )
        payload = query_params(
            labels=labels,
            maximum_instances=maximum_instances,
            minimum_instances=minimum_instances,
            name=name,
        )

        response = self._client.patch(url, json=payload)
        return response.json()["data"]

    def delete(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        kaas_worker_pool_id: int,
    ) -> bool:
        """
        Delete an instance pool from a Kubernetes service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.
            kaas_worker_pool_id: The unique identifier of the instance pool.

        Returns:
            bool: ``True`` when the delete request is accepted, otherwise ``False``.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/"
            f"kaas/{kaas_id}/instance_pools/{kaas_worker_pool_id}"
        )

        response = self._client.delete(url)
        return response.json()["data"]


class AsyncPools(AsyncResource):
    """Async cloud Kubernetes instance pool resources."""

    async def list(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        *,
        filter_: dict[str, Any] | None = None,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[dict[str, Any]]:
        """
        List all instance pools for a Kubernetes service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.
            filter_: Optional API filters.
            page: Optional page number for paginated responses.
            items: Optional number of items to return per page.

        Returns:
            plist[dict[str, Any]]: The list of instance pools and pagination metadata.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}/instance_pools"
        )
        params = query_params(filter=filter_, page=page, items=items)

        response = await self._client.get(url, params=params)
        payload = response.json()

        return plist(
            payload["data"],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )

    async def create(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        flavor: str,
        minimum_instances: int,
        name: str,
        *,
        availability_zone: str | None = None,
        labels: list[str] | None = None,
        maximum_instances: int | None = None,
        prefix: str | None = None,
    ) -> int:
        """
        Create an instance pool for a Kubernetes service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.
            flavor: The instance pool flavor.
            minimum_instances: The minimum number of instances.
            name: The instance pool name.
            availability_zone: Optional availability zone.
            labels: Optional Kubernetes labels to apply on instances.
            maximum_instances: Optional maximum number of instances.
            prefix: Optional prefix used when naming instances.

        Returns:
            int: The unique identifier of the newly created instance pool.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}/instance_pools"
        )
        payload: dict[str, Any] = {
            "flavor": flavor,
            "minimum_instances": minimum_instances,
            "name": name,
        }
        if availability_zone is not None:
            payload["availability_zone"] = availability_zone
        if labels is not None:
            payload["labels"] = labels
        if maximum_instances is not None:
            payload["maximum_instances"] = maximum_instances
        if prefix is not None:
            payload["prefix"] = prefix

        response = await self._client.post(url, json=payload)
        return response.json()["data"]

    async def get(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        kaas_worker_pool_id: int,
    ) -> dict[str, Any]:
        """
        Retrieve an instance pool from a Kubernetes service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.
            kaas_worker_pool_id: The unique identifier of the instance pool.

        Returns:
            dict[str, Any]: The instance pool details.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/"
            f"kaas/{kaas_id}/instance_pools/{kaas_worker_pool_id}"
        )
        response = await self._client.get(url)
        return response.json()["data"]

    async def update(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        kaas_worker_pool_id: int,
        *,
        labels: list[str] | None = None,
        maximum_instances: int | None = None,
        minimum_instances: int | None = None,
        name: str | None = None,
    ) -> bool:
        """
        Update an instance pool for a Kubernetes service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.
            kaas_worker_pool_id: The unique identifier of the instance pool.
            labels: Optional Kubernetes labels to apply on instances.
            maximum_instances: Optional maximum number of instances.
            minimum_instances: Optional minimum number of instances.
            name: Optional instance pool name.

        Returns:
            bool: ``True`` when the update request is accepted, otherwise ``False``.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/"
            f"kaas/{kaas_id}/instance_pools/{kaas_worker_pool_id}"
        )
        payload = query_params(
            labels=labels,
            maximum_instances=maximum_instances,
            minimum_instances=minimum_instances,
            name=name,
        )

        response = await self._client.patch(url, json=payload)
        return response.json()["data"]

    async def delete(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        kaas_worker_pool_id: int,
    ) -> bool:
        """
        Delete an instance pool from a Kubernetes service.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes service.
            kaas_worker_pool_id: The unique identifier of the instance pool.

        Returns:
            bool: ``True`` when the delete request is accepted, otherwise ``False``.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/"
            f"kaas/{kaas_id}/instance_pools/{kaas_worker_pool_id}"
        )

        response = await self._client.delete(url)
        return response.json()["data"]
