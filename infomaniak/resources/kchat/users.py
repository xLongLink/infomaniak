from infomaniak.resource import AsyncResource, Resouce


class UserRoles(Resouce):
    """kChat users roles endpoints."""

    def update(self) -> None:
        """Update a user's roles."""
        raise NotImplementedError("kChat users.roles.update endpoint is not implemented yet.")


class AsyncUserRoles(AsyncResource):
    """Async kChat users roles endpoints."""

    async def update(self) -> None:
        """Update a user's roles."""
        raise NotImplementedError("kChat users.roles.update endpoint is not implemented yet.")


class UserProfileImage(Resouce):
    """kChat users profile image endpoints."""

    def get(self) -> None:
        """Get user's profile image."""
        raise NotImplementedError("kChat users.profile.image.get endpoint is not implemented yet.")

    def default(self) -> None:
        """Return the default profile image."""
        raise NotImplementedError("kChat users.profile.image.default endpoint is not implemented yet.")


class AsyncUserProfileImage(AsyncResource):
    """Async kChat users profile image endpoints."""

    async def get(self) -> None:
        """Get user's profile image."""
        raise NotImplementedError("kChat users.profile.image.get endpoint is not implemented yet.")

    async def default(self) -> None:
        """Return the default profile image."""
        raise NotImplementedError("kChat users.profile.image.default endpoint is not implemented yet.")


class UserProfile(Resouce):
    """kChat users profile endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.image = UserProfileImage(client)


class AsyncUserProfile(AsyncResource):
    """Async kChat users profile endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.image = AsyncUserProfileImage(client)


class UserUsername(Resouce):
    """kChat users username endpoints."""

    def display(self) -> None:
        """Get a user by username."""
        raise NotImplementedError("kChat users.username.display endpoint is not implemented yet.")


class AsyncUserUsername(AsyncResource):
    """Async kChat users username endpoints."""

    async def display(self) -> None:
        """Get a user by username."""
        raise NotImplementedError("kChat users.username.display endpoint is not implemented yet.")


class UserEmail(Resouce):
    """kChat users email endpoints."""

    def display(self) -> None:
        """Get a user by email."""
        raise NotImplementedError("kChat users.email.display endpoint is not implemented yet.")


class AsyncUserEmail(AsyncResource):
    """Async kChat users email endpoints."""

    async def display(self) -> None:
        """Get a user by email."""
        raise NotImplementedError("kChat users.email.display endpoint is not implemented yet.")


class UserTyping(Resouce):
    """kChat users typing endpoints."""

    def publish(self) -> None:
        """Publish a typing WebSocket event."""
        raise NotImplementedError("kChat users.typing.publish endpoint is not implemented yet.")


class AsyncUserTyping(AsyncResource):
    """Async kChat users typing endpoints."""

    async def publish(self) -> None:
        """Publish a typing WebSocket event."""
        raise NotImplementedError("kChat users.typing.publish endpoint is not implemented yet.")


class UserChannels(Resouce):
    """kChat users channels endpoints."""

    def list(self) -> None:
        """List all channel memberships for a user."""
        raise NotImplementedError("kChat users.channels.list endpoint is not implemented yet.")


class AsyncUserChannels(AsyncResource):
    """Async kChat users channels endpoints."""

    async def list(self) -> None:
        """List all channel memberships for a user."""
        raise NotImplementedError("kChat users.channels.list endpoint is not implemented yet.")


class Users(Resouce):
    """kChat resource for users endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.roles = UserRoles(client)
        self.profile = UserProfile(client)
        self.username = UserUsername(client)
        self.email = UserEmail(client)
        self.typing = UserTyping(client)
        self.channels = UserChannels(client)

    def list(self) -> None:
        """List users."""
        raise NotImplementedError("kChat users.list endpoint is not implemented yet.")

    def by_ids(self) -> None:
        """Retrieve users by a list of IDs."""
        raise NotImplementedError("kChat users.by_ids endpoint is not implemented yet.")

    def by_group_channels_ids(self) -> None:
        """Retrieve users by group channel IDs."""
        raise NotImplementedError("kChat users.by_group_channels_ids endpoint is not implemented yet.")

    def by_usernames(self) -> None:
        """Retrieve users by usernames."""
        raise NotImplementedError("kChat users.by_usernames endpoint is not implemented yet.")

    def search(self) -> None:
        """Search users."""
        raise NotImplementedError("kChat users.search endpoint is not implemented yet.")

    def autocomplete(self) -> None:
        """Autocomplete user names."""
        raise NotImplementedError("kChat users.autocomplete endpoint is not implemented yet.")

    def display(self) -> None:
        """Get one user by ID."""
        raise NotImplementedError("kChat users.display endpoint is not implemented yet.")

    def patch(self) -> None:
        """Partially update a user."""
        raise NotImplementedError("kChat users.patch endpoint is not implemented yet.")


class AsyncUsers(AsyncResource):
    """Async kChat resource for users endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.roles = AsyncUserRoles(client)
        self.profile = AsyncUserProfile(client)
        self.username = AsyncUserUsername(client)
        self.email = AsyncUserEmail(client)
        self.typing = AsyncUserTyping(client)
        self.channels = AsyncUserChannels(client)

    async def list(self) -> None:
        """List users."""
        raise NotImplementedError("kChat users.list endpoint is not implemented yet.")

    async def by_ids(self) -> None:
        """Retrieve users by a list of IDs."""
        raise NotImplementedError("kChat users.by_ids endpoint is not implemented yet.")

    async def by_group_channels_ids(self) -> None:
        """Retrieve users by group channel IDs."""
        raise NotImplementedError("kChat users.by_group_channels_ids endpoint is not implemented yet.")

    async def by_usernames(self) -> None:
        """Retrieve users by usernames."""
        raise NotImplementedError("kChat users.by_usernames endpoint is not implemented yet.")

    async def search(self) -> None:
        """Search users."""
        raise NotImplementedError("kChat users.search endpoint is not implemented yet.")

    async def autocomplete(self) -> None:
        """Autocomplete user names."""
        raise NotImplementedError("kChat users.autocomplete endpoint is not implemented yet.")

    async def display(self) -> None:
        """Get one user by ID."""
        raise NotImplementedError("kChat users.display endpoint is not implemented yet.")

    async def patch(self) -> None:
        """Partially update a user."""
        raise NotImplementedError("kChat users.patch endpoint is not implemented yet.")


__all__ = [
    "Users",
    "AsyncUsers",
    "UserRoles",
    "AsyncUserRoles",
    "UserProfile",
    "AsyncUserProfile",
    "UserProfileImage",
    "AsyncUserProfileImage",
    "UserUsername",
    "AsyncUserUsername",
    "UserEmail",
    "AsyncUserEmail",
    "UserTyping",
    "AsyncUserTyping",
    "UserChannels",
    "AsyncUserChannels",
]
