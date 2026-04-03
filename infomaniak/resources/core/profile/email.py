from infomaniak.resource import AsyncResource, Resouce


class ProfileEmail(Resouce):
    """Core profile email endpoints."""

    def list(self) -> None:
        """List profile emails."""
        raise NotImplementedError("Core.profile.email.list is not implemented yet.")

    def display(self) -> None:
        """Display one profile email."""
        raise NotImplementedError("Core.profile.email.display is not implemented yet.")

    def delete(self) -> None:
        """Delete one profile email."""
        raise NotImplementedError("Core.profile.email.delete is not implemented yet.")


class AsyncProfileEmail(AsyncResource):
    """Async core profile email endpoints."""

    async def list(self) -> None:
        """List profile emails."""
        raise NotImplementedError("AsyncCore.profile.email.list is not implemented yet.")

    async def display(self) -> None:
        """Display one profile email."""
        raise NotImplementedError("AsyncCore.profile.email.display is not implemented yet.")

    async def delete(self) -> None:
        """Delete one profile email."""
        raise NotImplementedError("AsyncCore.profile.email.delete is not implemented yet.")
