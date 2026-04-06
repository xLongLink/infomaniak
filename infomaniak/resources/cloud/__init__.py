from __future__ import annotations

from .config import Config, AsyncConfig
from .database import Database, AsyncDatabase
from .projects import Projects, AsyncProjects
from .kubernetes import Kubernetes, AsyncKubernetes
from infomaniak.utils import parse, plist
from infomaniak.resource import Resouce, AsyncResource
from infomaniak.models.cloud import PublicCloud, PublicCloudBoolResponse


class Cloud(Resouce):
    """Cloud resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.config = Config(client)
        self.database = Database(client)
        self.kubernetes = Kubernetes(client)
        self.projects = Projects(client)

    def list(self, account_id: int) -> plist[PublicCloud]:
        """
        List all public cloud products linked to an account.

        Args:
            account_id: The unique identifier of the account related to the resource.

        Returns:
            plist[PublicCloud]: The list of public cloud products and pagination metadata.
        """
        response = self._client.get(
            "/1/public_clouds",
            params={"account_id": account_id},
        )
        payload = response.json()
        return plist(
            [parse(PublicCloud, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            items=payload.get("total") or 0,
        )

    def get(self, public_cloud_id: int) -> PublicCloud:
        """
        Retrieve a public cloud product.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.

        Returns:
            PublicCloud: The requested public cloud product details.
        """
        response = self._client.get(f"/1/public_clouds/{public_cloud_id}")
        return parse(PublicCloud, response.json()["data"])

    def update(
        self,
        public_cloud_id: int,
        *,
        bill_reference: str | None = None,
        customer_name: str | None = None,
        description: str | None = None,
    ) -> PublicCloudBoolResponse:
        """
        Update metadata of a public cloud product.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            bill_reference: Optional bill reference value.
            customer_name: Optional customer name.
            description: Optional public cloud description.

        Returns:
            PublicCloudBoolResponse: The API operation result with a boolean data payload.
        """
        payload = {
            "bill_reference": bill_reference,
            "customer_name": customer_name,
            "description": description,
        }
        response = self._client.patch(
            f"/1/public_clouds/{public_cloud_id}",
            json={key: value for key, value in payload.items() if value is not None},
        )
        return parse(PublicCloudBoolResponse, response.json())


class AsyncCloud(AsyncResource):
    """Async cloud resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.config = AsyncConfig(client)
        self.database = AsyncDatabase(client)
        self.kubernetes = AsyncKubernetes(client)
        self.projects = AsyncProjects(client)

    async def list(self, account_id: int) -> plist[PublicCloud]:
        """
        List all public cloud products linked to an account.

        Args:
            account_id: The unique identifier of the account related to the resource.

        Returns:
            plist[PublicCloud]: The list of public cloud products and pagination metadata.
        """
        response = await self._client.get(
            "/1/public_clouds",
            params={"account_id": account_id},
        )
        payload = response.json()
        return plist(
            [parse(PublicCloud, item) for item in payload["data"]],
            page=payload.get("page") or 1,
            pages=payload.get("pages") or 1,
            items=payload.get("total") or 0,
        )

    async def get(self, public_cloud_id: int) -> PublicCloud:
        """
        Retrieve a public cloud product.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.

        Returns:
            PublicCloud: The requested public cloud product details.
        """
        response = await self._client.get(f"/1/public_clouds/{public_cloud_id}")
        return parse(PublicCloud, response.json()["data"])

    async def update(
        self,
        public_cloud_id: int,
        *,
        bill_reference: str | None = None,
        customer_name: str | None = None,
        description: str | None = None,
    ) -> PublicCloudBoolResponse:
        """
        Update metadata of a public cloud product.

        Args:
            public_cloud_id: The unique identifier of the public cloud product.
            bill_reference: Optional bill reference value.
            customer_name: Optional customer name.
            description: Optional public cloud description.

        Returns:
            PublicCloudBoolResponse: The API operation result with a boolean data payload.
        """
        payload = {
            "bill_reference": bill_reference,
            "customer_name": customer_name,
            "description": description,
        }
        response = await self._client.patch(
            f"/1/public_clouds/{public_cloud_id}",
            json={key: value for key, value in payload.items() if value is not None},
        )
        return parse(PublicCloudBoolResponse, response.json())
