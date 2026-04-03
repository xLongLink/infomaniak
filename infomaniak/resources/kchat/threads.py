from infomaniak.resource import AsyncResource, Resouce


class Threads(Resouce):
    """kChat resource for threads endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for threads endpoints."""
        raise NotImplementedError("kChat threads endpoints are not implemented yet.")


class AsyncThreads(AsyncResource):
    """Async kChat resource for threads endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for threads endpoints."""
        raise NotImplementedError("kChat threads endpoints are not implemented yet.")
