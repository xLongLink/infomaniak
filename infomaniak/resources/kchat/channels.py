from infomaniak.resource import AsyncResource, Resouce


class Channels(Resouce):
    """kChat resource for channels endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for channels endpoints."""
        raise NotImplementedError("kChat channels endpoints are not implemented yet.")


class AsyncChannels(AsyncResource):
    """Async kChat resource for channels endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for channels endpoints."""
        raise NotImplementedError("kChat channels endpoints are not implemented yet.")
