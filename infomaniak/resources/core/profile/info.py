from infomaniak.resource import AsyncResource, Resouce


class ProfileInfo(Resouce):
    """Core profile info endpoints."""

    def list(self) -> None:
        """List profile information."""
        raise NotImplementedError("Core.profile.info.list is not implemented yet.")

    def update(self) -> None:
        """Update profile information."""
        raise NotImplementedError("Core.profile.info.update is not implemented yet.")


class AsyncProfileInfo(AsyncResource):
    """Async core profile info endpoints."""

    async def list(self) -> None:
        """List profile information."""
        raise NotImplementedError("AsyncCore.profile.info.list is not implemented yet.")

    async def update(self) -> None:
        """Update profile information."""
        raise NotImplementedError("AsyncCore.profile.info.update is not implemented yet.")
