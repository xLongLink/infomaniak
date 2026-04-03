from infomaniak.resource import AsyncResource, Resouce


class Events(Resouce):
    """Core events endpoints."""

    def list(self) -> None:
        """List events."""
        raise NotImplementedError("Core.events.list is not implemented yet.")

    def display(self) -> None:
        """Display one event."""
        raise NotImplementedError("Core.events.display is not implemented yet.")


class AsyncEvents(AsyncResource):
    """Async core events endpoints."""

    async def list(self) -> None:
        """List events."""
        raise NotImplementedError("AsyncCore.events.list is not implemented yet.")

    async def display(self) -> None:
        """Display one event."""
        raise NotImplementedError("AsyncCore.events.display is not implemented yet.")
