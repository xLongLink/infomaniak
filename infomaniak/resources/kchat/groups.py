from infomaniak.resource import AsyncResource, Resouce


class Groups(Resouce):
    """kChat resource for groups endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for groups endpoints."""
        raise NotImplementedError("kChat groups endpoints are not implemented yet.")


class AsyncGroups(AsyncResource):
    """Async kChat resource for groups endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for groups endpoints."""
        raise NotImplementedError("kChat groups endpoints are not implemented yet.")
