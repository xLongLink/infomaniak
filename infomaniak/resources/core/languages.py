from infomaniak.resource import AsyncResource, Resouce


class Languages(Resouce):
    """Core languages endpoints."""

    def list(self) -> None:
        """List languages."""
        raise NotImplementedError("Core.languages.list is not implemented yet.")

    def display(self) -> None:
        """Display one language."""
        raise NotImplementedError("Core.languages.display is not implemented yet.")


class AsyncLanguages(AsyncResource):
    """Async core languages endpoints."""

    async def list(self) -> None:
        """List languages."""
        raise NotImplementedError("AsyncCore.languages.list is not implemented yet.")

    async def display(self) -> None:
        """Display one language."""
        raise NotImplementedError("AsyncCore.languages.display is not implemented yet.")
