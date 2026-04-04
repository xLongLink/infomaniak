from infomaniak.resource import AsyncResource, Resouce


class Nameservers(Resouce):
    """DNS domain nameserver endpoints."""

    def update(self) -> None:
        """Update nameservers for a domain."""
        raise NotImplementedError("DNS.domain.nameservers.update is not implemented yet.")


class AsyncNameservers(AsyncResource):
    """Async DNS domain nameserver endpoints."""

    async def update(self) -> None:
        """Update nameservers for a domain."""
        raise NotImplementedError(
            "AsyncDNS.domain.nameservers.update is not implemented yet."
        )
