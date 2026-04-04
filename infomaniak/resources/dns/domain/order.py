from infomaniak.resource import AsyncResource, Resouce


class Order(Resouce):
    """DNS domain order endpoints."""

    def check(self) -> None:
        """Check whether a domain can be ordered."""
        raise NotImplementedError("DNS.domain.order.check is not implemented yet.")

    def create(self) -> None:
        """Create a domain order."""
        raise NotImplementedError("DNS.domain.order.create is not implemented yet.")

    def retry_create(self) -> None:
        """Retry the creation of a domain order."""
        raise NotImplementedError(
            "DNS.domain.order.retry_create is not implemented yet."
        )

    def transfer(self) -> None:
        """Transfer a domain."""
        raise NotImplementedError("DNS.domain.order.transfer is not implemented yet.")

    def retry_transfer(self) -> None:
        """Retry the transfer of a domain."""
        raise NotImplementedError(
            "DNS.domain.order.retry_transfer is not implemented yet."
        )


class AsyncOrder(AsyncResource):
    """Async DNS domain order endpoints."""

    async def check(self) -> None:
        """Check whether a domain can be ordered."""
        raise NotImplementedError("AsyncDNS.domain.order.check is not implemented yet.")

    async def create(self) -> None:
        """Create a domain order."""
        raise NotImplementedError("AsyncDNS.domain.order.create is not implemented yet.")

    async def retry_create(self) -> None:
        """Retry the creation of a domain order."""
        raise NotImplementedError(
            "AsyncDNS.domain.order.retry_create is not implemented yet."
        )

    async def transfer(self) -> None:
        """Transfer a domain."""
        raise NotImplementedError("AsyncDNS.domain.order.transfer is not implemented yet.")

    async def retry_transfer(self) -> None:
        """Retry the transfer of a domain."""
        raise NotImplementedError(
            "AsyncDNS.domain.order.retry_transfer is not implemented yet."
        )
