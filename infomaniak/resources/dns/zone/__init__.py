from infomaniak.resource import AsyncResource, Resouce

from .records import AsyncRecords, Records


class Zone(Resouce):
    """DNS zone endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.records = Records(client)

    def display(self) -> None:
        """Display one zone."""
        raise NotImplementedError("DNS.zone.display is not implemented yet.")

    def update(self) -> None:
        """Update one zone."""
        raise NotImplementedError("DNS.zone.update is not implemented yet.")

    def store(self) -> None:
        """Store one zone."""
        raise NotImplementedError("DNS.zone.store is not implemented yet.")

    def delete(self) -> None:
        """Delete one zone."""
        raise NotImplementedError("DNS.zone.delete is not implemented yet.")

    def exists(self) -> None:
        """Check whether one zone exists."""
        raise NotImplementedError("DNS.zone.exists is not implemented yet.")


class AsyncZone(AsyncResource):
    """Async DNS zone endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.records = AsyncRecords(client)

    async def display(self) -> None:
        """Display one zone."""
        raise NotImplementedError("AsyncDNS.zone.display is not implemented yet.")

    async def update(self) -> None:
        """Update one zone."""
        raise NotImplementedError("AsyncDNS.zone.update is not implemented yet.")

    async def store(self) -> None:
        """Store one zone."""
        raise NotImplementedError("AsyncDNS.zone.store is not implemented yet.")

    async def delete(self) -> None:
        """Delete one zone."""
        raise NotImplementedError("AsyncDNS.zone.delete is not implemented yet.")

    async def exists(self) -> None:
        """Check whether one zone exists."""
        raise NotImplementedError("AsyncDNS.zone.exists is not implemented yet.")


__all__ = [
    "Zone",
    "AsyncZone",
    "Records",
    "AsyncRecords",
]
