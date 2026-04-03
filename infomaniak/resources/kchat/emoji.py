from infomaniak.resource import AsyncResource, Resouce


class Emoji(Resouce):
    """kChat resource for emoji endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for emoji endpoints."""
        raise NotImplementedError("kChat emoji endpoints are not implemented yet.")


class AsyncEmoji(AsyncResource):
    """Async kChat resource for emoji endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for emoji endpoints."""
        raise NotImplementedError("kChat emoji endpoints are not implemented yet.")
