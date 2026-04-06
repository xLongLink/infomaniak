from __future__ import annotations

import random
from .ip import Ip, AsyncIp
from .data import Data, AsyncData
from typing import Any, Literal
from .pools import Pools, AsyncPools
from infomaniak.utils import plist, query_params
from infomaniak.resource import Resouce, AsyncResource


class Kubernetes(Resouce):
    """Cloud Kubernetes resources."""

    _DEFAULT_KUBERNETES_VERSION: Literal["1.32", "1.33", "1.34", "1.35"] = "1.35"
    _REGIONS: tuple[Literal["dc3-a", "dc4-a"], Literal["dc3-a", "dc4-a"]] = (
        "dc3-a",
        "dc4-a",
    )

    def __init__(self, client) -> None:
        super().__init__(client)
        self.data = Data(client)
        self.ip = Ip(client)
        self.pools = Pools(client)

    def list(
        self,
        public_cloud_id: int | None = None,
        public_cloud_project_id: int | None = None,
        *,
        account_id: int | None = None,
        with_: str | None = None,
        filter_: dict[str, Any] | None = None,
        return_: str | None = None,
        limit: int | None = None,
        skip: int | None = None,
        page: int | None = None,
        items: int | None = None,
        order_by: str | None = None,
        order: str | None = None,
        order_for: dict[str, str] | None = None,
    ) -> plist[dict[str, Any]]:
        """
        List Kubernetes clusters for a public cloud project or for an entire account.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project. If omitted,
                the account-wide endpoint is used.
            account_id: The unique identifier of the account. Required when
                ``public_cloud_project_id`` is omitted.
            with_: Optional expansion parameter.
            filter_: Optional API filters.
            return_: Optional return mode (for example ``total``).
            limit: Optional limit for offset-based pagination.
            skip: Optional offset for offset-based pagination.
            page: Optional page number for page-based pagination.
            items: Optional items per page for page-based pagination.
            order_by: Optional sort field.
            order: Optional sort direction.
            order_for: Optional per-field sort direction mapping.

        Returns:
            plist[dict[str, Any]]: The list of Kubernetes clusters and pagination metadata.
        """
        if public_cloud_project_id is None:
            if account_id is None:
                raise ValueError(
                    "account_id is required when public_cloud_project_id is not provided."
                )

            url = "/1/public_clouds/kaas"
            combined_filter = dict(filter_ or {})
            if public_cloud_id is not None:
                combined_filter.setdefault("public_cloud_id", public_cloud_id)
        else:
            if public_cloud_id is None:
                raise ValueError(
                    "public_cloud_id is required when public_cloud_project_id is provided."
                )

            url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/kaas"
            combined_filter = filter_

        params = query_params(
            account_id=account_id,
            filter=combined_filter,
            limit=limit,
            skip=skip,
            page=page,
            items=items,
            order_by=order_by,
            order=order,
            order_for=order_for,
            **{"with": with_, "return": return_},
        )

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
        name: str,
        kaas_pack: Literal["shared", "dedicated"] = "shared",
        kubernetes_version: Literal["1.29", "1.30", "1.31"] | None = None,
        region: Literal["dc3-a", "dc4-a"] | None = None,
    ) -> dict[str, Any]:
        """
        Create a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_pack: The Kubernetes service pack type. Use ``"shared"`` or
                ``"dedicated"``.
            kubernetes_version: The Kubernetes version. If omitted, the latest
                supported version is selected.
            name: The Kubernetes service name.
            region: The public cloud region. If omitted, a random supported
                region is selected.

        Returns:
            dict[str, Any]: The API response payload for the created cluster.
        """
        kaas_pack_id = 1 if kaas_pack == "shared" else 2
        selected_kubernetes_version = (
            kubernetes_version
            if kubernetes_version is not None
            else self._DEFAULT_KUBERNETES_VERSION
        )
        selected_region = region if region is not None else random.choice(self._REGIONS)

        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/kaas"
        response = self._client.post(
            url,
            json={
                "kaas_pack_id": kaas_pack_id,
                "kubernetes_version": selected_kubernetes_version,
                "name": name,
                "region": selected_region,
            },
        )
        return response.json()

    def get(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        *,
        with_: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes cluster.
            with_: Optional expansion parameter.

        Returns:
            dict[str, Any]: The Kubernetes cluster details.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}"
        )
        params = {"with": with_} if with_ is not None else None

        response = self._client.get(url, params=params)
        return response.json()["data"]

    def delete(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
    ) -> dict[str, Any]:
        """
        Delete a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes cluster.

        Returns:
            dict[str, Any]: The API operation result payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}"
        )
        response = self._client.delete(url)
        return response.json()

    def update(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Update a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes cluster.
            payload: The Kubernetes cluster update payload.

        Returns:
            dict[str, Any]: The API operation result payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}"
        )
        response = self._client.patch(url, json=payload)
        return response.json()

    def download(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
    ) -> dict[str, Any]:
        """
        Download a Kubernetes cluster kubeconfig payload.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes cluster.

        Returns:
            dict[str, Any]: The kubeconfig download payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/"
            f"kaas/{kaas_id}/kube_config"
        )
        response = self._client.get(url)
        return response.json()

    def patch(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Partially update a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes cluster.
            payload: The Kubernetes cluster patch payload.

        Returns:
            dict[str, Any]: The API operation result payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}"
        )
        response = self._client.patch(url, json=payload)
        return response.json()

    def kaas(
        self,
        *,
        account_id: int,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[dict[str, Any]]:
        """
        List available managed Kubernetes service templates.

        Args:
            account_id: Account identifier used to scope available templates.
            page: Optional page number for paginated responses.
            items: Optional number of items to return per page.

        Returns:
            plist[dict[str, Any]]: The list of available Kubernetes templates.
        """
        params: dict[str, int] = {"account_id": account_id}
        if page is not None:
            params["page"] = page
        if items is not None:
            params["items"] = items
        response = self._client.get("/1/public_clouds/kaas", params=params)
        payload = response.json()

        return plist(
            payload["data"],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
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
        public_cloud_id: int | None = None,
        public_cloud_project_id: int | None = None,
        *,
        account_id: int | None = None,
        with_: str | None = None,
        filter_: dict[str, Any] | None = None,
        return_: str | None = None,
        limit: int | None = None,
        skip: int | None = None,
        page: int | None = None,
        items: int | None = None,
        order_by: str | None = None,
        order: str | None = None,
        order_for: dict[str, str] | None = None,
    ) -> plist[dict[str, Any]]:
        """
        List Kubernetes clusters for a public cloud project or for an entire account.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project. If omitted,
                the account-wide endpoint is used.
            account_id: The unique identifier of the account. Required when
                ``public_cloud_project_id`` is omitted.
            with_: Optional expansion parameter.
            filter_: Optional API filters.
            return_: Optional return mode (for example ``total``).
            limit: Optional limit for offset-based pagination.
            skip: Optional offset for offset-based pagination.
            page: Optional page number for page-based pagination.
            items: Optional items per page for page-based pagination.
            order_by: Optional sort field.
            order: Optional sort direction.
            order_for: Optional per-field sort direction mapping.

        Returns:
            plist[dict[str, Any]]: The list of Kubernetes clusters and pagination metadata.
        """
        if public_cloud_project_id is None:
            if account_id is None:
                raise ValueError(
                    "account_id is required when public_cloud_project_id is not provided."
                )

            url = "/1/public_clouds/kaas"
            combined_filter = dict(filter_ or {})
            if public_cloud_id is not None:
                combined_filter.setdefault("public_cloud_id", public_cloud_id)
        else:
            if public_cloud_id is None:
                raise ValueError(
                    "public_cloud_id is required when public_cloud_project_id is provided."
                )

            url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/kaas"
            combined_filter = filter_

        params = query_params(
            account_id=account_id,
            filter=combined_filter,
            limit=limit,
            skip=skip,
            page=page,
            items=items,
            order_by=order_by,
            order=order,
            order_for=order_for,
            **{"with": with_, "return": return_},
        )

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
        name: str,
        kaas_pack: Literal["shared", "dedicated"] = "shared",
        kubernetes_version: Literal["1.29", "1.30", "1.31"] | None = None,
        region: Literal["dc3-a", "dc4-a"] | None = None,
    ) -> dict[str, Any]:
        """
        Create a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_pack: The Kubernetes service pack type. Use ``"shared"`` or
                ``"dedicated"``.
            kubernetes_version: The Kubernetes version. If omitted, the latest
                supported version is selected.
            name: The Kubernetes service name.
            region: The public cloud region. If omitted, a random supported
                region is selected.

        Returns:
            dict[str, Any]: The API response payload for the created cluster.
        """
        kaas_pack_id = 1 if kaas_pack == "shared" else 2
        selected_kubernetes_version = (
            kubernetes_version
            if kubernetes_version is not None
            else Kubernetes._DEFAULT_KUBERNETES_VERSION
        )
        selected_region = (
            region if region is not None else random.choice(Kubernetes._REGIONS)
        )

        url = f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/kaas"
        response = await self._client.post(
            url,
            json={
                "kaas_pack_id": kaas_pack_id,
                "kubernetes_version": selected_kubernetes_version,
                "name": name,
                "region": selected_region,
            },
        )
        return response.json()

    async def get(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        *,
        with_: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes cluster.
            with_: Optional expansion parameter.

        Returns:
            dict[str, Any]: The Kubernetes cluster details.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}"
        )
        params = {"with": with_} if with_ is not None else None

        response = await self._client.get(url, params=params)
        return response.json()["data"]

    async def delete(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
    ) -> dict[str, Any]:
        """
        Delete a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes cluster.

        Returns:
            dict[str, Any]: The API operation result payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}"
        )
        response = await self._client.delete(url)
        return response.json()

    async def update(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Update a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes cluster.
            payload: The Kubernetes cluster update payload.

        Returns:
            dict[str, Any]: The API operation result payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}"
        )
        response = await self._client.patch(url, json=payload)
        return response.json()

    async def download(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
    ) -> dict[str, Any]:
        """
        Download a Kubernetes cluster kubeconfig payload.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes cluster.

        Returns:
            dict[str, Any]: The kubeconfig download payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/{public_cloud_project_id}/"
            f"kaas/{kaas_id}/kube_config"
        )
        response = await self._client.get(url)
        return response.json()

    async def patch(
        self,
        public_cloud_id: int,
        public_cloud_project_id: int,
        kaas_id: int,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Partially update a Kubernetes cluster.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            public_cloud_project_id: The unique identifier of the public cloud project.
            kaas_id: The unique identifier of the Kubernetes cluster.
            payload: The Kubernetes cluster patch payload.

        Returns:
            dict[str, Any]: The API operation result payload.
        """
        url = (
            f"/1/public_clouds/{public_cloud_id}/projects/"
            f"{public_cloud_project_id}/kaas/{kaas_id}"
        )
        response = await self._client.patch(url, json=payload)
        return response.json()

    async def kaas(
        self,
        *,
        account_id: int,
        page: int | None = None,
        items: int | None = None,
    ) -> plist[dict[str, Any]]:
        """
        List available managed Kubernetes service templates.

        Args:
            account_id: Account identifier used to scope available templates.
            page: Optional page number for paginated responses.
            items: Optional number of items to return per page.

        Returns:
            plist[dict[str, Any]]: The list of available Kubernetes templates.
        """
        params: dict[str, int] = {"account_id": account_id}
        if page is not None:
            params["page"] = page
        if items is not None:
            params["items"] = items
        response = await self._client.get("/1/public_clouds/kaas", params=params)
        payload = response.json()

        return plist(
            payload["data"],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            total=payload.get("total") or 0,
        )
