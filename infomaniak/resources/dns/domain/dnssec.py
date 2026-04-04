from infomaniak.resource import AsyncResource, Resouce


class DNSSEC(Resouce):
    """DNS domain DNSSEC endpoints."""

    def check(self) -> None:
        """Check DNSSEC status for a domain."""
        raise NotImplementedError("DNS.domain.dnssec.check is not implemented yet.")

    def enable(self) -> None:
        """Enable DNSSEC for a domain."""
        raise NotImplementedError("DNS.domain.dnssec.enable is not implemented yet.")

    def disable(self) -> None:
        """Disable DNSSEC for a domain."""
        raise NotImplementedError("DNS.domain.dnssec.disable is not implemented yet.")


class AsyncDNSSEC(AsyncResource):
    """Async DNS domain DNSSEC endpoints."""

    async def check(self) -> None:
        """Check DNSSEC status for a domain."""
        raise NotImplementedError("AsyncDNS.domain.dnssec.check is not implemented yet.")

    async def enable(self) -> None:
        """Enable DNSSEC for a domain."""
        raise NotImplementedError("AsyncDNS.domain.dnssec.enable is not implemented yet.")

    async def disable(self) -> None:
        """Disable DNSSEC for a domain."""
        raise NotImplementedError("AsyncDNS.domain.dnssec.disable is not implemented yet.")
