from infomaniak.resource import AsyncResource, Resouce


class Users(Resouce):
    """kChat resource for users endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for users endpoints."""
        raise NotImplementedError("kChat users endpoints are not implemented yet.")


class AsyncUsers(AsyncResource):
    """Async kChat resource for users endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for users endpoints."""
        raise NotImplementedError("kChat users endpoints are not implemented yet.")
