from infomaniak.resource import AsyncResource, Resouce


class Teams(Resouce):
    """kChat resource for teams endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for teams endpoints."""
        raise NotImplementedError("kChat teams endpoints are not implemented yet.")


class AsyncTeams(AsyncResource):
    """Async kChat resource for teams endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for teams endpoints."""
        raise NotImplementedError("kChat teams endpoints are not implemented yet.")
