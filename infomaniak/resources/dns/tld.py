from infomaniak.resource import AsyncResource, Resouce


class TLD(Resouce):
    """DNS TLD endpoints."""

    def list(self) -> None:
        """List available TLDs."""
        raise NotImplementedError("DNS.tld.list is not implemented yet.")

    def display(self) -> None:
        """Display one TLD."""
        raise NotImplementedError("DNS.tld.display is not implemented yet.")


class AsyncTLD(AsyncResource):
    """Async DNS TLD endpoints."""

    async def list(self) -> None:
        """List available TLDs."""
        raise NotImplementedError("AsyncDNS.tld.list is not implemented yet.")

    async def display(self) -> None:
        """Display one TLD."""
        raise NotImplementedError("AsyncDNS.tld.display is not implemented yet.")
