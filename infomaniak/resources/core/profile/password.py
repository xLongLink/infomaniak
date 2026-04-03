from infomaniak.resource import AsyncResource, Resouce


class ProfilePassword(Resouce):
    """Core profile password endpoints."""

    def list(self) -> None:
        """List profile password rules."""
        raise NotImplementedError("Core.profile.password.list is not implemented yet.")

    def add(self) -> None:
        """Add profile password."""
        raise NotImplementedError("Core.profile.password.add is not implemented yet.")

    def display(self) -> None:
        """Display profile password details."""
        raise NotImplementedError("Core.profile.password.display is not implemented yet.")


class AsyncProfilePassword(AsyncResource):
    """Async core profile password endpoints."""

    async def list(self) -> None:
        """List profile password rules."""
        raise NotImplementedError("AsyncCore.profile.password.list is not implemented yet.")

    async def add(self) -> None:
        """Add profile password."""
        raise NotImplementedError("AsyncCore.profile.password.add is not implemented yet.")

    async def display(self) -> None:
        """Display profile password details."""
        raise NotImplementedError("AsyncCore.profile.password.display is not implemented yet.")
