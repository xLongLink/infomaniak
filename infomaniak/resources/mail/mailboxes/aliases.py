from infomaniak.resource import AsyncResource, Resouce


class Aliases(Resouce):
    """Mailbox aliases endpoints."""

    def list(self) -> None:
        """List aliases for a mailbox."""
        raise NotImplementedError("Mailbox aliases list endpoint is not implemented yet.")

    def update(self) -> None:
        """Replace aliases for a mailbox."""
        raise NotImplementedError("Mailbox aliases update endpoint is not implemented yet.")

    def add(self) -> None:
        """Add an alias to a mailbox."""
        raise NotImplementedError("Mailbox aliases add endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete an alias from a mailbox."""
        raise NotImplementedError("Mailbox aliases delete endpoint is not implemented yet.")


class AsyncAliases(AsyncResource):
    """Async mailbox aliases endpoints."""

    async def list(self) -> None:
        """List aliases for a mailbox."""
        raise NotImplementedError("Mailbox aliases list endpoint is not implemented yet.")

    async def update(self) -> None:
        """Replace aliases for a mailbox."""
        raise NotImplementedError("Mailbox aliases update endpoint is not implemented yet.")

    async def add(self) -> None:
        """Add an alias to a mailbox."""
        raise NotImplementedError("Mailbox aliases add endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete an alias from a mailbox."""
        raise NotImplementedError("Mailbox aliases delete endpoint is not implemented yet.")


__all__ = ["Aliases", "AsyncAliases"]
