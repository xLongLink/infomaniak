from infomaniak.resource import AsyncResource, Resouce


class Products(Resouce):
    """Core products endpoints."""

    def list(self) -> None:
        """List products."""
        raise NotImplementedError("Core.products.list is not implemented yet.")


class AsyncProducts(AsyncResource):
    """Async core products endpoints."""

    async def list(self) -> None:
        """List products."""
        raise NotImplementedError("AsyncCore.products.list is not implemented yet.")
