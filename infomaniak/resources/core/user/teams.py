from infomaniak.resource import AsyncResource, Resouce


class UserTeams(Resouce):
    """Core user teams endpoints."""

    def list(self) -> None:
        """List user teams."""
        raise NotImplementedError("Core.user.teams.list is not implemented yet.")

    def create(self) -> None:
        """Create a user team."""
        raise NotImplementedError("Core.user.teams.create is not implemented yet.")

    def get(self) -> None:
        """Get a user team."""
        raise NotImplementedError("Core.user.teams.get is not implemented yet.")

    def delete(self) -> None:
        """Delete a user team."""
        raise NotImplementedError("Core.user.teams.delete is not implemented yet.")

    def update(self) -> None:
        """Update a user team."""
        raise NotImplementedError("Core.user.teams.update is not implemented yet.")


class AsyncUserTeams(AsyncResource):
    """Async core user teams endpoints."""

    async def list(self) -> None:
        """List user teams."""
        raise NotImplementedError("AsyncCore.user.teams.list is not implemented yet.")

    async def create(self) -> None:
        """Create a user team."""
        raise NotImplementedError("AsyncCore.user.teams.create is not implemented yet.")

    async def get(self) -> None:
        """Get a user team."""
        raise NotImplementedError("AsyncCore.user.teams.get is not implemented yet.")

    async def delete(self) -> None:
        """Delete a user team."""
        raise NotImplementedError("AsyncCore.user.teams.delete is not implemented yet.")

    async def update(self) -> None:
        """Update a user team."""
        raise NotImplementedError("AsyncCore.user.teams.update is not implemented yet.")
