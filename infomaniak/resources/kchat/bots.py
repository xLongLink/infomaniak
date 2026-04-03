from infomaniak.resource import AsyncResource, Resouce


class Bots(Resouce):
    """kChat resource for bots endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for bots endpoints."""
        raise NotImplementedError("kChat bots endpoints are not implemented yet.")


class AsyncBots(AsyncResource):
    """Async kChat resource for bots endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for bots endpoints."""
        raise NotImplementedError("kChat bots endpoints are not implemented yet.")
