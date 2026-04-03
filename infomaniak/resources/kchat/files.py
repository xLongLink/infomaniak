from infomaniak.resource import AsyncResource, Resouce


class Files(Resouce):
    """kChat resource for files endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for files endpoints."""
        raise NotImplementedError("kChat files endpoints are not implemented yet.")


class AsyncFiles(AsyncResource):
    """Async kChat resource for files endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for files endpoints."""
        raise NotImplementedError("kChat files endpoints are not implemented yet.")
