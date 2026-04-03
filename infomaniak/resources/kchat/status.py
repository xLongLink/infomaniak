from infomaniak.resource import AsyncResource, Resouce


class Status(Resouce):
    """kChat resource for status endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for status endpoints."""
        raise NotImplementedError("kChat status endpoints are not implemented yet.")


class AsyncStatus(AsyncResource):
    """Async kChat resource for status endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for status endpoints."""
        raise NotImplementedError("kChat status endpoints are not implemented yet.")
