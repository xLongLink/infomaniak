from infomaniak.resource import AsyncResource, Resouce


class SubscribersAddressbooks(Resouce):
    """Newsletter subscribers addressbooks endpoints."""

    def list(self) -> None:
        """List subscriber address books."""
        raise NotImplementedError(
            "Newsletter subscribers addressbooks list endpoint is not implemented yet."
        )

    def select(self) -> None:
        """Select subscriber address books."""
        raise NotImplementedError(
            "Newsletter subscribers addressbooks select endpoint is not implemented yet."
        )


class AsyncSubscribersAddressbooks(AsyncResource):
    """Async newsletter subscribers addressbooks endpoints."""

    async def list(self) -> None:
        """List subscriber address books."""
        raise NotImplementedError(
            "Newsletter subscribers addressbooks list endpoint is not implemented yet."
        )

    async def select(self) -> None:
        """Select subscriber address books."""
        raise NotImplementedError(
            "Newsletter subscribers addressbooks select endpoint is not implemented yet."
        )


__all__ = ["SubscribersAddressbooks", "AsyncSubscribersAddressbooks"]
