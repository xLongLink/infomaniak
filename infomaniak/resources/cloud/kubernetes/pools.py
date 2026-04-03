from infomaniak.resource import AsyncResource, Resouce


class Pools(Resouce):
    """Cloud Kubernetes worker pool resources."""

    def list(self) -> None:
        """List Kubernetes worker pools."""
        raise NotImplementedError("Cloud Kubernetes pools list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a Kubernetes worker pool."""
        raise NotImplementedError("Cloud Kubernetes pools create endpoint is not implemented yet.")

    def get(self) -> None:
        """Retrieve a Kubernetes worker pool."""
        raise NotImplementedError("Cloud Kubernetes pools get endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a Kubernetes worker pool."""
        raise NotImplementedError("Cloud Kubernetes pools update endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a Kubernetes worker pool."""
        raise NotImplementedError("Cloud Kubernetes pools delete endpoint is not implemented yet.")


class AsyncPools(AsyncResource):
    """Async cloud Kubernetes worker pool resources."""

    async def list(self) -> None:
        """List Kubernetes worker pools."""
        raise NotImplementedError("Cloud Kubernetes pools list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a Kubernetes worker pool."""
        raise NotImplementedError("Cloud Kubernetes pools create endpoint is not implemented yet.")

    async def get(self) -> None:
        """Retrieve a Kubernetes worker pool."""
        raise NotImplementedError("Cloud Kubernetes pools get endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a Kubernetes worker pool."""
        raise NotImplementedError("Cloud Kubernetes pools update endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a Kubernetes worker pool."""
        raise NotImplementedError("Cloud Kubernetes pools delete endpoint is not implemented yet.")


__all__ = ["Pools", "AsyncPools"]
