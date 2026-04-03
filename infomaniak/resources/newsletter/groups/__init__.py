from infomaniak.resource import AsyncResource, Resouce

from .subscribers import AsyncGroupsSubscribers, GroupsSubscribers


class Groups(Resouce):
    """Newsletter groups endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.subscribers = GroupsSubscribers(client)

    def list(self) -> None:
        """List all groups."""
        raise NotImplementedError("Newsletter groups list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a group."""
        raise NotImplementedError("Newsletter groups create endpoint is not implemented yet.")

    def delete_bulk(self) -> None:
        """Delete multiple groups."""
        raise NotImplementedError("Newsletter groups delete_bulk endpoint is not implemented yet.")

    def display(self) -> None:
        """Get a specific group."""
        raise NotImplementedError("Newsletter groups display endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a group."""
        raise NotImplementedError("Newsletter groups update endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a group."""
        raise NotImplementedError("Newsletter groups delete endpoint is not implemented yet.")


class AsyncGroups(AsyncResource):
    """Async newsletter groups endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.subscribers = AsyncGroupsSubscribers(client)

    async def list(self) -> None:
        """List all groups."""
        raise NotImplementedError("Newsletter groups list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a group."""
        raise NotImplementedError("Newsletter groups create endpoint is not implemented yet.")

    async def delete_bulk(self) -> None:
        """Delete multiple groups."""
        raise NotImplementedError("Newsletter groups delete_bulk endpoint is not implemented yet.")

    async def display(self) -> None:
        """Get a specific group."""
        raise NotImplementedError("Newsletter groups display endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a group."""
        raise NotImplementedError("Newsletter groups update endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a group."""
        raise NotImplementedError("Newsletter groups delete endpoint is not implemented yet.")


__all__ = ["Groups", "AsyncGroups", "GroupsSubscribers", "AsyncGroupsSubscribers"]
