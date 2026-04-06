from __future__ import annotations

from infomaniak.utils import parse
from infomaniak.resource import Resouce, AsyncResource
from infomaniak.models.cloud import PublicCloudConfig


class Config(Resouce):
    """Public cloud configuration endpoints."""

    def get(self, account_id: int) -> PublicCloudConfig:
        """
        Get configuration information for a public cloud account.

        Args:
            account_id: The unique identifier of the account related to the resource.

        Returns:
            PublicCloudConfig: The public cloud account configuration.
        """
        response = self._client.get(
            "/1/public_clouds/config",
            params={"account_id": account_id},
        )
        return parse(PublicCloudConfig, response.json()["data"])


class AsyncConfig(AsyncResource):
    """Async public cloud configuration endpoints."""

    async def get(self, account_id: int) -> PublicCloudConfig:
        """
        Get configuration information for a public cloud account.

        Args:
            account_id: The unique identifier of the account related to the resource.

        Returns:
            PublicCloudConfig: The public cloud account configuration.
        """
        response = await self._client.get(
            "/1/public_clouds/config",
            params={"account_id": account_id},
        )
        return parse(PublicCloudConfig, response.json()["data"])
