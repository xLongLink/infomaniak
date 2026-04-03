from infomaniak.resource import AsyncResource, Resouce


class Credits(Resouce):
    """Newsletter credits endpoints."""

    def list(self) -> None:
        """List all credits."""
        raise NotImplementedError("Newsletter credits list endpoint is not implemented yet.")

    def display(self) -> None:
        """Get credits of a specific account."""
        raise NotImplementedError("Newsletter credits display endpoint is not implemented yet.")


class AsyncCredits(AsyncResource):
    """Async newsletter credits endpoints."""

    async def list(self) -> None:
        """List all credits."""
        raise NotImplementedError("Newsletter credits list endpoint is not implemented yet.")

    async def display(self) -> None:
        """Get credits of a specific account."""
        raise NotImplementedError("Newsletter credits display endpoint is not implemented yet.")


__all__ = ["Credits", "AsyncCredits"]
