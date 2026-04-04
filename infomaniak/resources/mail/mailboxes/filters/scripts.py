from infomaniak.resource import AsyncResource, Resouce


class Scripts(Resouce):
    """Mailbox sieve script endpoints."""

    def add(self) -> None:
        """Add a mailbox sieve script."""
        raise NotImplementedError("Mailbox filter scripts add endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a mailbox sieve script."""
        raise NotImplementedError("Mailbox filter scripts delete endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a mailbox sieve script."""
        raise NotImplementedError("Mailbox filter scripts update endpoint is not implemented yet.")

    def set_activation(self) -> None:
        """Enable or disable a mailbox sieve script."""
        raise NotImplementedError("Mailbox filter scripts set_activation endpoint is not implemented yet.")


class AsyncScripts(AsyncResource):
    """Async mailbox sieve script endpoints."""

    async def add(self) -> None:
        """Add a mailbox sieve script."""
        raise NotImplementedError("Mailbox filter scripts add endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a mailbox sieve script."""
        raise NotImplementedError("Mailbox filter scripts delete endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a mailbox sieve script."""
        raise NotImplementedError("Mailbox filter scripts update endpoint is not implemented yet.")

    async def set_activation(self) -> None:
        """Enable or disable a mailbox sieve script."""
        raise NotImplementedError("Mailbox filter scripts set_activation endpoint is not implemented yet.")


__all__ = ["Scripts", "AsyncScripts"]
