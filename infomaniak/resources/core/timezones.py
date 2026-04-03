from infomaniak.resource import AsyncResource, Resouce


class Timezones(Resouce):
    """Core timezones endpoints."""

    def list(self) -> None:
        """List timezones."""
        raise NotImplementedError("Core.timezones.list is not implemented yet.")

    def display(self) -> None:
        """Display one timezone."""
        raise NotImplementedError("Core.timezones.display is not implemented yet.")


class AsyncTimezones(AsyncResource):
    """Async core timezones endpoints."""

    async def list(self) -> None:
        """List timezones."""
        raise NotImplementedError("AsyncCore.timezones.list is not implemented yet.")

    async def display(self) -> None:
        """Display one timezone."""
        raise NotImplementedError("AsyncCore.timezones.display is not implemented yet.")
