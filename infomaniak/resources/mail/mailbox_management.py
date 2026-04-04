from infomaniak.resource import AsyncResource, Resouce


class MailboxManagement(Resouce):
    """Mailbox management endpoints."""

    def list(self) -> None:
        """List existing mailboxes."""
        raise NotImplementedError("Mailbox management list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a mailbox."""
        raise NotImplementedError("Mailbox management create endpoint is not implemented yet.")

    def display(self) -> None:
        """Display a mailbox by name or ID."""
        raise NotImplementedError("Mailbox management display endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a mailbox."""
        raise NotImplementedError("Mailbox management update endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a mailbox."""
        raise NotImplementedError("Mailbox management delete endpoint is not implemented yet.")


class AsyncMailboxManagement(AsyncResource):
    """Async mailbox management endpoints."""

    async def list(self) -> None:
        """List existing mailboxes."""
        raise NotImplementedError("Mailbox management list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a mailbox."""
        raise NotImplementedError("Mailbox management create endpoint is not implemented yet.")

    async def display(self) -> None:
        """Display a mailbox by name or ID."""
        raise NotImplementedError("Mailbox management display endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a mailbox."""
        raise NotImplementedError("Mailbox management update endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a mailbox."""
        raise NotImplementedError("Mailbox management delete endpoint is not implemented yet.")


__all__ = ["MailboxManagement", "AsyncMailboxManagement"]
