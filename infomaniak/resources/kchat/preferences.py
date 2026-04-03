from infomaniak.resource import AsyncResource, Resouce


class Preferences(Resouce):
    """kChat resource for preferences endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for preferences endpoints."""
        raise NotImplementedError("kChat preferences endpoints are not implemented yet.")


class AsyncPreferences(AsyncResource):
    """Async kChat resource for preferences endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for preferences endpoints."""
        raise NotImplementedError("kChat preferences endpoints are not implemented yet.")
