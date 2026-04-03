from infomaniak.resource import AsyncResource, Resouce


class Ip(Resouce):
    """Cloud Kubernetes API server IP filter resources."""

    def list(self) -> None:
        """List Kubernetes API server IP filters."""
        raise NotImplementedError("Cloud Kubernetes IP list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a Kubernetes API server IP filter."""
        raise NotImplementedError("Cloud Kubernetes IP create endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a Kubernetes API server IP filter."""
        raise NotImplementedError("Cloud Kubernetes IP update endpoint is not implemented yet.")

    def remove(self) -> None:
        """Remove a Kubernetes API server IP filter."""
        raise NotImplementedError("Cloud Kubernetes IP remove endpoint is not implemented yet.")


class AsyncIp(AsyncResource):
    """Async cloud Kubernetes API server IP filter resources."""

    async def list(self) -> None:
        """List Kubernetes API server IP filters."""
        raise NotImplementedError("Cloud Kubernetes IP list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a Kubernetes API server IP filter."""
        raise NotImplementedError("Cloud Kubernetes IP create endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a Kubernetes API server IP filter."""
        raise NotImplementedError("Cloud Kubernetes IP update endpoint is not implemented yet.")

    async def remove(self) -> None:
        """Remove a Kubernetes API server IP filter."""
        raise NotImplementedError("Cloud Kubernetes IP remove endpoint is not implemented yet.")


__all__ = ["Ip", "AsyncIp"]
