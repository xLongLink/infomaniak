from infomaniak.resource import AsyncResource, Resouce


class Records(Resouce):
    """DNS zone records endpoints."""

    def list(self) -> None:
        """List DNS records for one zone."""
        raise NotImplementedError("DNS.zone.records.list is not implemented yet.")

    def store(self) -> None:
        """Store a DNS record."""
        raise NotImplementedError("DNS.zone.records.store is not implemented yet.")

    def display(self) -> None:
        """Display one DNS record."""
        raise NotImplementedError("DNS.zone.records.display is not implemented yet.")

    def update(self) -> None:
        """Update one DNS record."""
        raise NotImplementedError("DNS.zone.records.update is not implemented yet.")

    def delete(self) -> None:
        """Delete one DNS record."""
        raise NotImplementedError("DNS.zone.records.delete is not implemented yet.")

    def check(self) -> None:
        """Check whether a DNS record exists and resolves."""
        raise NotImplementedError("DNS.zone.records.check is not implemented yet.")


class AsyncRecords(AsyncResource):
    """Async DNS zone records endpoints."""

    async def list(self) -> None:
        """List DNS records for one zone."""
        raise NotImplementedError("AsyncDNS.zone.records.list is not implemented yet.")

    async def store(self) -> None:
        """Store a DNS record."""
        raise NotImplementedError("AsyncDNS.zone.records.store is not implemented yet.")

    async def display(self) -> None:
        """Display one DNS record."""
        raise NotImplementedError("AsyncDNS.zone.records.display is not implemented yet.")

    async def update(self) -> None:
        """Update one DNS record."""
        raise NotImplementedError("AsyncDNS.zone.records.update is not implemented yet.")

    async def delete(self) -> None:
        """Delete one DNS record."""
        raise NotImplementedError("AsyncDNS.zone.records.delete is not implemented yet.")

    async def check(self) -> None:
        """Check whether a DNS record exists and resolves."""
        raise NotImplementedError("AsyncDNS.zone.records.check is not implemented yet.")
