from infomaniak.resource import AsyncResource, Resouce


class Actions(Resouce):
    """Core actions endpoints."""

    def list(self) -> None:
        """List actions."""
        raise NotImplementedError("Core.actions.list is not implemented yet.")


class AsyncActions(AsyncResource):
    """Async core actions endpoints."""

    async def list(self) -> None:
        """List actions."""
        raise NotImplementedError("AsyncCore.actions.list is not implemented yet.")
