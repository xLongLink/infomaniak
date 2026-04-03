from infomaniak.resource import AsyncResource, Resouce


class System(Resouce):
    """kChat resource for system endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for system endpoints."""
        raise NotImplementedError("kChat system endpoints are not implemented yet.")


class AsyncSystem(AsyncResource):
    """Async kChat resource for system endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for system endpoints."""
        raise NotImplementedError("kChat system endpoints are not implemented yet.")
