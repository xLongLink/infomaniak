from infomaniak.resource import AsyncResource, Resouce


class GroupsSubscribers(Resouce):
    """Newsletter group subscribers endpoints."""

    def list(self) -> None:
        """List subscribers in a group."""
        raise NotImplementedError(
            "Newsletter groups subscribers list endpoint is not implemented yet."
        )

    def assign(self) -> None:
        """Assign subscribers to a group."""
        raise NotImplementedError(
            "Newsletter groups subscribers assign endpoint is not implemented yet."
        )

    def unassign(self) -> None:
        """Unassign subscribers from a group."""
        raise NotImplementedError(
            "Newsletter groups subscribers unassign endpoint is not implemented yet."
        )


class AsyncGroupsSubscribers(AsyncResource):
    """Async newsletter group subscribers endpoints."""

    async def list(self) -> None:
        """List subscribers in a group."""
        raise NotImplementedError(
            "Newsletter groups subscribers list endpoint is not implemented yet."
        )

    async def assign(self) -> None:
        """Assign subscribers to a group."""
        raise NotImplementedError(
            "Newsletter groups subscribers assign endpoint is not implemented yet."
        )

    async def unassign(self) -> None:
        """Unassign subscribers from a group."""
        raise NotImplementedError(
            "Newsletter groups subscribers unassign endpoint is not implemented yet."
        )


__all__ = ["GroupsSubscribers", "AsyncGroupsSubscribers"]
