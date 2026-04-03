from infomaniak.resource import AsyncResource, Resouce


class Countries(Resouce):
    """Core countries endpoints."""

    def list(self) -> None:
        """List countries."""
        raise NotImplementedError("Core.countries.list is not implemented yet.")

    def display(self) -> None:
        """Display one country."""
        raise NotImplementedError("Core.countries.display is not implemented yet.")


class AsyncCountries(AsyncResource):
    """Async core countries endpoints."""

    async def list(self) -> None:
        """List countries."""
        raise NotImplementedError("AsyncCore.countries.list is not implemented yet.")

    async def display(self) -> None:
        """Display one country."""
        raise NotImplementedError("AsyncCore.countries.display is not implemented yet.")
