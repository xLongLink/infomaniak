from __future__ import annotations

from .ip import Ip, AsyncIp
from .data import Data, AsyncData
from typing import Any
from .pools import Pools, AsyncPools
from infomaniak.utils import PaginatedList
from infomaniak.resource import Resouce, AsyncResource


class Kubernetes(Resouce):
    """Cloud Kubernetes resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.data = Data(client)
        self.ip = Ip(client)
        self.pools = Pools(client)

    def list(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        *,
        with_: str | None = None,
    ) -> PaginatedList[dict[str, Any]]:
        """
        List Kubernetes clusters for a public cloud project.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            with_: Optional expansion parameter.

        Returns:
            PaginatedList[dict[str, Any]]: The list of Kubernetes clusters and pagination metadata.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/kubernetes"
        params = {"with": with_} if with_ is not None else None

        response = self._client.get(url, params=params)
        payload = response.json()

        return PaginatedList(
            payload["data"],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            items=payload.get("total") or 0,
        )

    def create(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Create a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            payload: The Kubernetes cluster creation payload.

        Returns:
            dict[str, Any]: The API response payload for the created cluster.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/kubernetes"
        response = self._client.post(url, json=payload)
        return response.json()

    def get(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kubernetes_id: int,
        *,
        with_: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kubernetes_id: The unique identifier of the Kubernetes cluster.
            with_: Optional expansion parameter.

        Returns:
            dict[str, Any]: The Kubernetes cluster details.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kubernetes/{kubernetes_id}"
        )
        params = {"with": with_} if with_ is not None else None

        response = self._client.get(url, params=params)
        return response.json()["data"]

    def delete(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kubernetes_id: int,
    ) -> dict[str, Any]:
        """
        Delete a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kubernetes_id: The unique identifier of the Kubernetes cluster.

        Returns:
            dict[str, Any]: The API operation result payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kubernetes/{kubernetes_id}"
        )
        response = self._client.delete(url)
        return response.json()

    def update(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kubernetes_id: int,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Update a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kubernetes_id: The unique identifier of the Kubernetes cluster.
            payload: The Kubernetes cluster update payload.

        Returns:
            dict[str, Any]: The API operation result payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kubernetes/{kubernetes_id}"
        )
        response = self._client.put(url, json=payload)
        return response.json()

    def download(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kubernetes_id: int,
    ) -> dict[str, Any]:
        """
        Download a Kubernetes cluster kubeconfig payload.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kubernetes_id: The unique identifier of the Kubernetes cluster.

        Returns:
            dict[str, Any]: The kubeconfig download payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/"
            f"kubernetes/{kubernetes_id}/download"
        )
        response = self._client.get(url)
        return response.json()

    def patch(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kubernetes_id: int,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Partially update a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kubernetes_id: The unique identifier of the Kubernetes cluster.
            payload: The Kubernetes cluster patch payload.

        Returns:
            dict[str, Any]: The API operation result payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kubernetes/{kubernetes_id}"
        )
        response = self._client.patch(url, json=payload)
        return response.json()

    def kaas(self, *, account_id: int | None = None) -> PaginatedList[dict[str, Any]]:
        """
        List available managed Kubernetes service templates.

        Args:
            account_id: Optional account identifier used to scope available templates.

        Returns:
            PaginatedList[dict[str, Any]]: The list of available Kubernetes templates.
        """
        params = {"account_id": account_id} if account_id is not None else None
        response = self._client.get("/1/public_clouds/kaas", params=params)
        payload = response.json()

        return PaginatedList(
            payload["data"],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            items=payload.get("total") or 0,
        )


class AsyncKubernetes(AsyncResource):
    """Async cloud Kubernetes resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.data = AsyncData(client)
        self.ip = AsyncIp(client)
        self.pools = AsyncPools(client)

    async def list(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        *,
        with_: str | None = None,
    ) -> PaginatedList[dict[str, Any]]:
        """
        List Kubernetes clusters for a public cloud project.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            with_: Optional expansion parameter.

        Returns:
            PaginatedList[dict[str, Any]]: The list of Kubernetes clusters and pagination metadata.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/kubernetes"
        params = {"with": with_} if with_ is not None else None

        response = await self._client.get(url, params=params)
        payload = response.json()

        return PaginatedList(
            payload["data"],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            items=payload.get("total") or 0,
        )

    async def create(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Create a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            payload: The Kubernetes cluster creation payload.

        Returns:
            dict[str, Any]: The API response payload for the created cluster.
        """
        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/kubernetes"
        response = await self._client.post(url, json=payload)
        return response.json()

    async def get(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kubernetes_id: int,
        *,
        with_: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kubernetes_id: The unique identifier of the Kubernetes cluster.
            with_: Optional expansion parameter.

        Returns:
            dict[str, Any]: The Kubernetes cluster details.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kubernetes/{kubernetes_id}"
        )
        params = {"with": with_} if with_ is not None else None

        response = await self._client.get(url, params=params)
        return response.json()["data"]

    async def delete(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kubernetes_id: int,
    ) -> dict[str, Any]:
        """
        Delete a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kubernetes_id: The unique identifier of the Kubernetes cluster.

        Returns:
            dict[str, Any]: The API operation result payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kubernetes/{kubernetes_id}"
        )
        response = await self._client.delete(url)
        return response.json()

    async def update(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kubernetes_id: int,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Update a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kubernetes_id: The unique identifier of the Kubernetes cluster.
            payload: The Kubernetes cluster update payload.

        Returns:
            dict[str, Any]: The API operation result payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kubernetes/{kubernetes_id}"
        )
        response = await self._client.put(url, json=payload)
        return response.json()

    async def download(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kubernetes_id: int,
    ) -> dict[str, Any]:
        """
        Download a Kubernetes cluster kubeconfig payload.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kubernetes_id: The unique identifier of the Kubernetes cluster.

        Returns:
            dict[str, Any]: The kubeconfig download payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/"
            f"kubernetes/{kubernetes_id}/download"
        )
        response = await self._client.get(url)
        return response.json()

    async def patch(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kubernetes_id: int,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Partially update a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kubernetes_id: The unique identifier of the Kubernetes cluster.
            payload: The Kubernetes cluster patch payload.

        Returns:
            dict[str, Any]: The API operation result payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kubernetes/{kubernetes_id}"
        )
        response = await self._client.patch(url, json=payload)
        return response.json()

    async def kaas(self, *, account_id: int | None = None) -> PaginatedList[dict[str, Any]]:
        """
        List available managed Kubernetes service templates.

        Args:
            account_id: Optional account identifier used to scope available templates.

        Returns:
            PaginatedList[dict[str, Any]]: The list of available Kubernetes templates.
        """
        params = {"account_id": account_id} if account_id is not None else None
        response = await self._client.get("/1/public_clouds/kaas", params=params)
        payload = response.json()

        return PaginatedList(
            payload["data"],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            items=payload.get("total") or 0,
        )
