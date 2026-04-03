from infomaniak.resource import AsyncResource, Resouce

from .data import AsyncData, Data
from .ip import AsyncIp, Ip
from .pools import AsyncPools, Pools


class Kubernetes(Resouce):
    """Cloud Kubernetes resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.data = Data(client)
        self.ip = Ip(client)
        self.pools = Pools(client)

    def list(self) -> None:
        """List Kubernetes clusters."""
        raise NotImplementedError("Cloud Kubernetes list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a Kubernetes cluster."""
        raise NotImplementedError("Cloud Kubernetes create endpoint is not implemented yet.")

    def get(self) -> None:
        """Retrieve a Kubernetes cluster."""
        raise NotImplementedError("Cloud Kubernetes get endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a Kubernetes cluster."""
        raise NotImplementedError("Cloud Kubernetes delete endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a Kubernetes cluster."""
        raise NotImplementedError("Cloud Kubernetes update endpoint is not implemented yet.")

    def download(self) -> None:
        """Download Kubernetes cluster kubeconfig."""
        raise NotImplementedError("Cloud Kubernetes download endpoint is not implemented yet.")

    def patch(self) -> None:
        """Patch a Kubernetes cluster."""
        raise NotImplementedError("Cloud Kubernetes patch endpoint is not implemented yet.")

    def kaas(self) -> None:
        """List available Kubernetes service templates."""
        raise NotImplementedError("Cloud Kubernetes kaas endpoint is not implemented yet.")


class AsyncKubernetes(AsyncResource):
    """Async cloud Kubernetes resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.data = AsyncData(client)
        self.ip = AsyncIp(client)
        self.pools = AsyncPools(client)

    async def list(self) -> None:
        """List Kubernetes clusters."""
        raise NotImplementedError("Cloud Kubernetes list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a Kubernetes cluster."""
        raise NotImplementedError("Cloud Kubernetes create endpoint is not implemented yet.")

    async def get(self) -> None:
        """Retrieve a Kubernetes cluster."""
        raise NotImplementedError("Cloud Kubernetes get endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a Kubernetes cluster."""
        raise NotImplementedError("Cloud Kubernetes delete endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a Kubernetes cluster."""
        raise NotImplementedError("Cloud Kubernetes update endpoint is not implemented yet.")

    async def download(self) -> None:
        """Download Kubernetes cluster kubeconfig."""
        raise NotImplementedError("Cloud Kubernetes download endpoint is not implemented yet.")

    async def patch(self) -> None:
        """Patch a Kubernetes cluster."""
        raise NotImplementedError("Cloud Kubernetes patch endpoint is not implemented yet.")

    async def kaas(self) -> None:
        """List available Kubernetes service templates."""
        raise NotImplementedError("Cloud Kubernetes kaas endpoint is not implemented yet.")


__all__ = [
    "Data",
    "Ip",
    "Pools",
    "AsyncData",
    "AsyncIp",
    "AsyncPools",
    "Kubernetes",
    "AsyncKubernetes",
]
