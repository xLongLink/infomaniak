from infomaniak.resource import AsyncResource, Resouce


class ProfileAvatar(Resouce):
    """Core profile avatar endpoints."""

    def update(self) -> None:
        """Update profile avatar."""
        raise NotImplementedError("Core.profile.avatar.update is not implemented yet.")

    def delete(self) -> None:
        """Delete profile avatar."""
        raise NotImplementedError("Core.profile.avatar.delete is not implemented yet.")


class AsyncProfileAvatar(AsyncResource):
    """Async core profile avatar endpoints."""

    async def update(self) -> None:
        """Update profile avatar."""
        raise NotImplementedError("AsyncCore.profile.avatar.update is not implemented yet.")

    async def delete(self) -> None:
        """Delete profile avatar."""
        raise NotImplementedError("AsyncCore.profile.avatar.delete is not implemented yet.")
