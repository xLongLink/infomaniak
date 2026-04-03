from infomaniak.resource import AsyncResource, Resouce


class TeamMembersRoles(Resouce):
    """kChat teams members roles endpoints."""

    def update(self) -> None:
        """Update a team member's roles."""
        raise NotImplementedError("kChat teams.members.roles.update endpoint is not implemented yet.")


class AsyncTeamMembersRoles(AsyncResource):
    """Async kChat teams members roles endpoints."""

    async def update(self) -> None:
        """Update a team member's roles."""
        raise NotImplementedError("kChat teams.members.roles.update endpoint is not implemented yet.")


class TeamMembers(Resouce):
    """kChat teams members endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.roles = TeamMembersRoles(client)

    def list(self) -> None:
        """List members of a team."""
        raise NotImplementedError("kChat teams.members.list endpoint is not implemented yet.")

    def for_user(self) -> None:
        """List team memberships for a user."""
        raise NotImplementedError("kChat teams.members.for_user endpoint is not implemented yet.")

    def display(self) -> None:
        """Get a team member."""
        raise NotImplementedError("kChat teams.members.display endpoint is not implemented yet.")

    def by_ids(self) -> None:
        """Get team members by IDs."""
        raise NotImplementedError("kChat teams.members.by_ids endpoint is not implemented yet.")


class AsyncTeamMembers(AsyncResource):
    """Async kChat teams members endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.roles = AsyncTeamMembersRoles(client)

    async def list(self) -> None:
        """List members of a team."""
        raise NotImplementedError("kChat teams.members.list endpoint is not implemented yet.")

    async def for_user(self) -> None:
        """List team memberships for a user."""
        raise NotImplementedError("kChat teams.members.for_user endpoint is not implemented yet.")

    async def display(self) -> None:
        """Get a team member."""
        raise NotImplementedError("kChat teams.members.display endpoint is not implemented yet.")

    async def by_ids(self) -> None:
        """Get team members by IDs."""
        raise NotImplementedError("kChat teams.members.by_ids endpoint is not implemented yet.")


class TeamUnreads(Resouce):
    """kChat teams unreads endpoints."""

    def __call__(self) -> None:
        """Get unreads for a team."""
        raise NotImplementedError("kChat teams.unreads endpoint is not implemented yet.")

    def for_user(self) -> None:
        """Get team unreads for a user."""
        raise NotImplementedError("kChat teams.unreads.for_user endpoint is not implemented yet.")


class AsyncTeamUnreads(AsyncResource):
    """Async kChat teams unreads endpoints."""

    async def __call__(self) -> None:
        """Get unreads for a team."""
        raise NotImplementedError("kChat teams.unreads endpoint is not implemented yet.")

    async def for_user(self) -> None:
        """Get team unreads for a user."""
        raise NotImplementedError("kChat teams.unreads.for_user endpoint is not implemented yet.")


class TeamFiles(Resouce):
    """kChat teams files endpoints."""

    def search(self) -> None:
        """Search files in a team."""
        raise NotImplementedError("kChat teams.files.search endpoint is not implemented yet.")


class AsyncTeamFiles(AsyncResource):
    """Async kChat teams files endpoints."""

    async def search(self) -> None:
        """Search files in a team."""
        raise NotImplementedError("kChat teams.files.search endpoint is not implemented yet.")


class Teams(Resouce):
    """kChat resource for teams endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.members = TeamMembers(client)
        self.unreads = TeamUnreads(client)
        self.files = TeamFiles(client)

    def list(self) -> None:
        """List teams."""
        raise NotImplementedError("kChat teams.list endpoint is not implemented yet.")

    def display(self) -> None:
        """Get a team by ID."""
        raise NotImplementedError("kChat teams.display endpoint is not implemented yet.")

    def by_name(self) -> None:
        """Get a team by name."""
        raise NotImplementedError("kChat teams.by_name endpoint is not implemented yet.")

    def user_teams(self) -> None:
        """List the teams of a user."""
        raise NotImplementedError("kChat teams.user_teams endpoint is not implemented yet.")

    def stats(self) -> None:
        """Get team statistics."""
        raise NotImplementedError("kChat teams.stats endpoint is not implemented yet.")

    def invite_guests(self) -> None:
        """Invite guests to a team."""
        raise NotImplementedError("kChat teams.invite_guests endpoint is not implemented yet.")


class AsyncTeams(AsyncResource):
    """Async kChat resource for teams endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.members = AsyncTeamMembers(client)
        self.unreads = AsyncTeamUnreads(client)
        self.files = AsyncTeamFiles(client)

    async def list(self) -> None:
        """List teams."""
        raise NotImplementedError("kChat teams.list endpoint is not implemented yet.")

    async def display(self) -> None:
        """Get a team by ID."""
        raise NotImplementedError("kChat teams.display endpoint is not implemented yet.")

    async def by_name(self) -> None:
        """Get a team by name."""
        raise NotImplementedError("kChat teams.by_name endpoint is not implemented yet.")

    async def user_teams(self) -> None:
        """List the teams of a user."""
        raise NotImplementedError("kChat teams.user_teams endpoint is not implemented yet.")

    async def stats(self) -> None:
        """Get team statistics."""
        raise NotImplementedError("kChat teams.stats endpoint is not implemented yet.")

    async def invite_guests(self) -> None:
        """Invite guests to a team."""
        raise NotImplementedError("kChat teams.invite_guests endpoint is not implemented yet.")
