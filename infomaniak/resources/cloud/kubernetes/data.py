from infomaniak.resource import AsyncResource, Resouce


class Data(Resouce):
    """Cloud Kubernetes reference data resources."""

    def list(self) -> None:
        """List available Kubernetes reference datasets."""
        raise NotImplementedError("Cloud Kubernetes data list endpoint is not implemented yet.")

    def versions(self) -> None:
        """List available Kubernetes versions."""
        raise NotImplementedError("Cloud Kubernetes data versions endpoint is not implemented yet.")

    def regions(self) -> None:
        """List available Kubernetes regions."""
        raise NotImplementedError("Cloud Kubernetes data regions endpoint is not implemented yet.")

    def reagions(self) -> None:
        """Compatibility alias for regions()."""
        return self.regions()

    def zones(self) -> None:
        """List available Kubernetes availability zones."""
        raise NotImplementedError("Cloud Kubernetes data zones endpoint is not implemented yet.")

    def flavors(self) -> None:
        """List available Kubernetes flavors."""
        raise NotImplementedError("Cloud Kubernetes data flavors endpoint is not implemented yet.")


class AsyncData(AsyncResource):
    """Async cloud Kubernetes reference data resources."""

    async def list(self) -> None:
        """List available Kubernetes reference datasets."""
        raise NotImplementedError("Cloud Kubernetes data list endpoint is not implemented yet.")

    async def versions(self) -> None:
        """List available Kubernetes versions."""
        raise NotImplementedError("Cloud Kubernetes data versions endpoint is not implemented yet.")

    async def regions(self) -> None:
        """List available Kubernetes regions."""
        raise NotImplementedError("Cloud Kubernetes data regions endpoint is not implemented yet.")

    async def reagions(self) -> None:
        """Compatibility alias for regions()."""
        return await self.regions()

    async def zones(self) -> None:
        """List available Kubernetes availability zones."""
        raise NotImplementedError("Cloud Kubernetes data zones endpoint is not implemented yet.")

    async def flavors(self) -> None:
        """List available Kubernetes flavors."""
        raise NotImplementedError("Cloud Kubernetes data flavors endpoint is not implemented yet.")


__all__ = ["Data", "AsyncData"]
