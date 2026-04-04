from infomaniak.resource import AsyncResource, Resouce

from .scripts import AsyncScripts, Scripts


class Filters(Resouce):
    """Mailbox sieve filter endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.scripts = Scripts(client)

    def list(self) -> None:
        """List sieve filters and scripts for a mailbox."""
        raise NotImplementedError("Mailbox filters list endpoint is not implemented yet.")

    def set_activation(self) -> None:
        """Enable or disable a mailbox filter."""
        raise NotImplementedError("Mailbox filters set_activation endpoint is not implemented yet.")

    def reorder(self) -> None:
        """Reorder mailbox filters."""
        raise NotImplementedError("Mailbox filters reorder endpoint is not implemented yet.")

    def add(self) -> None:
        """Add a mailbox filter."""
        raise NotImplementedError("Mailbox filters add endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a mailbox filter."""
        raise NotImplementedError("Mailbox filters delete endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a mailbox filter."""
        raise NotImplementedError("Mailbox filters update endpoint is not implemented yet.")


class AsyncFilters(AsyncResource):
    """Async mailbox sieve filter endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.scripts = AsyncScripts(client)

    async def list(self) -> None:
        """List sieve filters and scripts for a mailbox."""
        raise NotImplementedError("Mailbox filters list endpoint is not implemented yet.")

    async def set_activation(self) -> None:
        """Enable or disable a mailbox filter."""
        raise NotImplementedError("Mailbox filters set_activation endpoint is not implemented yet.")

    async def reorder(self) -> None:
        """Reorder mailbox filters."""
        raise NotImplementedError("Mailbox filters reorder endpoint is not implemented yet.")

    async def add(self) -> None:
        """Add a mailbox filter."""
        raise NotImplementedError("Mailbox filters add endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a mailbox filter."""
        raise NotImplementedError("Mailbox filters delete endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a mailbox filter."""
        raise NotImplementedError("Mailbox filters update endpoint is not implemented yet.")


__all__ = ["Filters", "AsyncFilters", "Scripts", "AsyncScripts"]
