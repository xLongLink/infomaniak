from infomaniak.resource import AsyncResource, Resouce


class Tasks(Resouce):
    """Core tasks endpoints."""

    def list(self) -> None:
        """List tasks."""
        raise NotImplementedError("Core.tasks.list is not implemented yet.")

    def display(self) -> None:
        """Display one task."""
        raise NotImplementedError("Core.tasks.display is not implemented yet.")


class AsyncTasks(AsyncResource):
    """Async core tasks endpoints."""

    async def list(self) -> None:
        """List tasks."""
        raise NotImplementedError("AsyncCore.tasks.list is not implemented yet.")

    async def display(self) -> None:
        """Display one task."""
        raise NotImplementedError("AsyncCore.tasks.display is not implemented yet.")
