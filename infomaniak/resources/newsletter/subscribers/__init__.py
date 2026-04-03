from infomaniak.resource import AsyncResource, Resouce

from .addressbooks import AsyncSubscribersAddressbooks, SubscribersAddressbooks


class Subscribers(Resouce):
    """Newsletter subscribers endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.addressbooks = SubscribersAddressbooks(client)

    def list(self) -> None:
        """List all subscribers."""
        raise NotImplementedError("Newsletter subscribers list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a subscriber."""
        raise NotImplementedError("Newsletter subscribers create endpoint is not implemented yet.")

    def delete_bulk(self) -> None:
        """Bulk delete subscribers."""
        raise NotImplementedError(
            "Newsletter subscribers delete_bulk endpoint is not implemented yet."
        )

    def count_status(self) -> None:
        """Count subscribers by status."""
        raise NotImplementedError(
            "Newsletter subscribers count_status endpoint is not implemented yet."
        )

    def display(self) -> None:
        """Get subscriber details."""
        raise NotImplementedError("Newsletter subscribers display endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a subscriber."""
        raise NotImplementedError("Newsletter subscribers update endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a subscriber."""
        raise NotImplementedError("Newsletter subscribers delete endpoint is not implemented yet.")

    def filter(self) -> None:
        """Filter subscribers."""
        raise NotImplementedError("Newsletter subscribers filter endpoint is not implemented yet.")

    def export(self) -> None:
        """Export subscribers."""
        raise NotImplementedError("Newsletter subscribers export endpoint is not implemented yet.")

    def import_(self) -> None:
        """Import subscribers."""
        raise NotImplementedError("Newsletter subscribers import_ endpoint is not implemented yet.")

    def upload_csv(self) -> None:
        """Upload a CSV file."""
        raise NotImplementedError("Newsletter subscribers upload_csv endpoint is not implemented yet.")

    def forget(self) -> None:
        """Forget a subscriber (GDPR)."""
        raise NotImplementedError("Newsletter subscribers forget endpoint is not implemented yet.")

    def unsubscribe(self) -> None:
        """Unsubscribe subscribers."""
        raise NotImplementedError("Newsletter subscribers unsubscribe endpoint is not implemented yet.")

    def assign(self) -> None:
        """Assign subscribers to a group."""
        raise NotImplementedError("Newsletter subscribers assign endpoint is not implemented yet.")

    def unassign(self) -> None:
        """Unassign subscribers from a group."""
        raise NotImplementedError("Newsletter subscribers unassign endpoint is not implemented yet.")


class AsyncSubscribers(AsyncResource):
    """Async newsletter subscribers endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.addressbooks = AsyncSubscribersAddressbooks(client)

    async def list(self) -> None:
        """List all subscribers."""
        raise NotImplementedError("Newsletter subscribers list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a subscriber."""
        raise NotImplementedError("Newsletter subscribers create endpoint is not implemented yet.")

    async def delete_bulk(self) -> None:
        """Bulk delete subscribers."""
        raise NotImplementedError(
            "Newsletter subscribers delete_bulk endpoint is not implemented yet."
        )

    async def count_status(self) -> None:
        """Count subscribers by status."""
        raise NotImplementedError(
            "Newsletter subscribers count_status endpoint is not implemented yet."
        )

    async def display(self) -> None:
        """Get subscriber details."""
        raise NotImplementedError("Newsletter subscribers display endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a subscriber."""
        raise NotImplementedError("Newsletter subscribers update endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a subscriber."""
        raise NotImplementedError("Newsletter subscribers delete endpoint is not implemented yet.")

    async def filter(self) -> None:
        """Filter subscribers."""
        raise NotImplementedError("Newsletter subscribers filter endpoint is not implemented yet.")

    async def export(self) -> None:
        """Export subscribers."""
        raise NotImplementedError("Newsletter subscribers export endpoint is not implemented yet.")

    async def import_(self) -> None:
        """Import subscribers."""
        raise NotImplementedError("Newsletter subscribers import_ endpoint is not implemented yet.")

    async def upload_csv(self) -> None:
        """Upload a CSV file."""
        raise NotImplementedError("Newsletter subscribers upload_csv endpoint is not implemented yet.")

    async def forget(self) -> None:
        """Forget a subscriber (GDPR)."""
        raise NotImplementedError("Newsletter subscribers forget endpoint is not implemented yet.")

    async def unsubscribe(self) -> None:
        """Unsubscribe subscribers."""
        raise NotImplementedError("Newsletter subscribers unsubscribe endpoint is not implemented yet.")

    async def assign(self) -> None:
        """Assign subscribers to a group."""
        raise NotImplementedError("Newsletter subscribers assign endpoint is not implemented yet.")

    async def unassign(self) -> None:
        """Unassign subscribers from a group."""
        raise NotImplementedError("Newsletter subscribers unassign endpoint is not implemented yet.")


__all__ = [
    "Subscribers",
    "AsyncSubscribers",
    "SubscribersAddressbooks",
    "AsyncSubscribersAddressbooks",
]
