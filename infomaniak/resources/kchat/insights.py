from infomaniak.resource import AsyncResource, Resouce


class Insights(Resouce):
    """kChat resource for insights endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for insights endpoints."""
        raise NotImplementedError("kChat insights endpoints are not implemented yet.")


class AsyncInsights(AsyncResource):
    """Async kChat resource for insights endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for insights endpoints."""
        raise NotImplementedError("kChat insights endpoints are not implemented yet.")
