from infomaniak.resource import AsyncResource, Resouce


class Administrator(Resouce):
    """Swiss Backup administrator management endpoints."""

    def update(self) -> None:
        """Update the administrator for a Swiss Backup product."""
        raise NotImplementedError("Backup.administrator.update is not implemented yet.")

    def create(self) -> None:
        """Create a new administrator for a Swiss Backup product."""
        raise NotImplementedError("Backup.administrator.create is not implemented yet.")


class AsyncAdministrator(AsyncResource):
    """Async Swiss Backup administrator management endpoints."""

    async def update(self) -> None:
        """Update the administrator for a Swiss Backup product."""
        raise NotImplementedError("AsyncBackup.administrator.update is not implemented yet.")

    async def create(self) -> None:
        """Create a new administrator for a Swiss Backup product."""
        raise NotImplementedError("AsyncBackup.administrator.create is not implemented yet.")


__all__ = ["Administrator", "AsyncAdministrator"]
