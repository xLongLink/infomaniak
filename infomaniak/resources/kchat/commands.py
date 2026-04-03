from infomaniak.resource import AsyncResource, Resouce


class Commands(Resouce):
    """kChat resource for commands endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for commands endpoints."""
        raise NotImplementedError("kChat commands endpoints are not implemented yet.")


class AsyncCommands(AsyncResource):
    """Async kChat resource for commands endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for commands endpoints."""
        raise NotImplementedError("kChat commands endpoints are not implemented yet.")
