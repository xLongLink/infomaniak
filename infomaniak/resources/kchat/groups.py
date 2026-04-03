from infomaniak.resource import AsyncResource, Resouce


class Groups(Resouce):
    """kChat resource for groups endpoints."""

    def list(self) -> None:
        """List all groups."""
        raise NotImplementedError("kChat groups.list endpoint is not implemented yet.")

    def channel_groups(self) -> None:
        """Get groups linked to a channel."""
        raise NotImplementedError("kChat groups.channel_groups endpoint is not implemented yet.")

    def team_groups(self) -> None:
        """Get groups linked to a team."""
        raise NotImplementedError("kChat groups.team_groups endpoint is not implemented yet.")

    def team_channel_groups(self) -> None:
        """Get groups in a team grouped by channels."""
        raise NotImplementedError("kChat groups.team_channel_groups endpoint is not implemented yet.")

    def user_groups(self) -> None:
        """Get groups for a user."""
        raise NotImplementedError("kChat groups.user_groups endpoint is not implemented yet.")


class AsyncGroups(AsyncResource):
    """Async kChat resource for groups endpoints."""

    async def list(self) -> None:
        """List all groups."""
        raise NotImplementedError("kChat groups.list endpoint is not implemented yet.")

    async def channel_groups(self) -> None:
        """Get groups linked to a channel."""
        raise NotImplementedError("kChat groups.channel_groups endpoint is not implemented yet.")

    async def team_groups(self) -> None:
        """Get groups linked to a team."""
        raise NotImplementedError("kChat groups.team_groups endpoint is not implemented yet.")

    async def team_channel_groups(self) -> None:
        """Get groups in a team grouped by channels."""
        raise NotImplementedError("kChat groups.team_channel_groups endpoint is not implemented yet.")

    async def user_groups(self) -> None:
        """Get groups for a user."""
        raise NotImplementedError("kChat groups.user_groups endpoint is not implemented yet.")
