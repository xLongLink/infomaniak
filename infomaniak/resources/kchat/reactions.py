from infomaniak.resource import AsyncResource, Resouce


class Reactions(Resouce):
    """kChat resource for reactions endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for reactions endpoints."""
        raise NotImplementedError("kChat reactions endpoints are not implemented yet.")


class AsyncReactions(AsyncResource):
    """Async kChat resource for reactions endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for reactions endpoints."""
        raise NotImplementedError("kChat reactions endpoints are not implemented yet.")
