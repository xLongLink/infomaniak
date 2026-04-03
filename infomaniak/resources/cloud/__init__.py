from infomaniak.resource import AsyncResource, Resouce

from .database import AsyncDatabase, Database
from .kubernetes import AsyncKubernetes, Kubernetes


class Cloud(Resouce):
    """Cloud resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.database = Database(client)
        self.kubernetes = Kubernetes(client)

    def config(self) -> None:
        """Cloud resource for configuration endpoints."""
        raise NotImplementedError("Cloud config endpoint is not implemented yet.")


class AsyncCloud(AsyncResource):
    """Async cloud resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.database = AsyncDatabase(client)
        self.kubernetes = AsyncKubernetes(client)

    async def config(self) -> None:
        """Async cloud resource for configuration endpoints."""
        raise NotImplementedError("Cloud config endpoint is not implemented yet.")


__all__ = [
    "Database",
    "Kubernetes",
    "AsyncDatabase",
    "AsyncKubernetes",
    "Cloud",
    "AsyncCloud",
]
