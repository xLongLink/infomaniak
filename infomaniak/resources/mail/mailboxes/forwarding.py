from infomaniak.resource import AsyncResource, Resouce


class Forwarding(Resouce):
    """Mailbox forwarding endpoints."""

    def list(self) -> None:
        """List forwarding addresses for a mailbox."""
        raise NotImplementedError("Mailbox forwarding list endpoint is not implemented yet.")

    def update(self) -> None:
        """Update forwarding configuration for a mailbox."""
        raise NotImplementedError("Mailbox forwarding update endpoint is not implemented yet.")

    def add(self) -> None:
        """Add a forwarding address to a mailbox."""
        raise NotImplementedError("Mailbox forwarding add endpoint is not implemented yet.")

    def delete_all(self) -> None:
        """Delete all forwarding addresses for a mailbox."""
        raise NotImplementedError("Mailbox forwarding delete_all endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a forwarding address for a mailbox."""
        raise NotImplementedError("Mailbox forwarding delete endpoint is not implemented yet.")


class AsyncForwarding(AsyncResource):
    """Async mailbox forwarding endpoints."""

    async def list(self) -> None:
        """List forwarding addresses for a mailbox."""
        raise NotImplementedError("Mailbox forwarding list endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update forwarding configuration for a mailbox."""
        raise NotImplementedError("Mailbox forwarding update endpoint is not implemented yet.")

    async def add(self) -> None:
        """Add a forwarding address to a mailbox."""
        raise NotImplementedError("Mailbox forwarding add endpoint is not implemented yet.")

    async def delete_all(self) -> None:
        """Delete all forwarding addresses for a mailbox."""
        raise NotImplementedError("Mailbox forwarding delete_all endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a forwarding address for a mailbox."""
        raise NotImplementedError("Mailbox forwarding delete endpoint is not implemented yet.")


__all__ = ["Forwarding", "AsyncForwarding"]
