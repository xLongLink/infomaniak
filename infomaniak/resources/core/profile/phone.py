from infomaniak.resource import AsyncResource, Resouce


class ProfilePhone(Resouce):
    """Core profile phone endpoints."""

    def list(self) -> None:
        """List profile phones."""
        raise NotImplementedError("Core.profile.phone.list is not implemented yet.")

    def display(self) -> None:
        """Display one profile phone."""
        raise NotImplementedError("Core.profile.phone.display is not implemented yet.")

    def delete(self) -> None:
        """Delete one profile phone."""
        raise NotImplementedError("Core.profile.phone.delete is not implemented yet.")


class AsyncProfilePhone(AsyncResource):
    """Async core profile phone endpoints."""

    async def list(self) -> None:
        """List profile phones."""
        raise NotImplementedError("AsyncCore.profile.phone.list is not implemented yet.")

    async def display(self) -> None:
        """Display one profile phone."""
        raise NotImplementedError("AsyncCore.profile.phone.display is not implemented yet.")

    async def delete(self) -> None:
        """Delete one profile phone."""
        raise NotImplementedError("AsyncCore.profile.phone.delete is not implemented yet.")
