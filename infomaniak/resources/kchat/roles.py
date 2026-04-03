from infomaniak.resource import AsyncResource, Resouce


class Roles(Resouce):
    """kChat resource for roles endpoints."""

    def non_implemented(self) -> None:
        """Placeholder for roles endpoints."""
        raise NotImplementedError("kChat roles endpoints are not implemented yet.")


class AsyncRoles(AsyncResource):
    """Async kChat resource for roles endpoints."""

    async def non_implemented(self) -> None:
        """Placeholder for roles endpoints."""
        raise NotImplementedError("kChat roles endpoints are not implemented yet.")
