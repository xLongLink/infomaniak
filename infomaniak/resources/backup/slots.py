from infomaniak.resource import AsyncResource, Resouce


class Slots(Resouce):
    """Swiss Backup slot management endpoints."""

    def list(self) -> None:
        """List all backup slots."""
        raise NotImplementedError("Backup.slots.list is not implemented yet.")

    def create(self) -> None:
        """Create a new backup slot."""
        raise NotImplementedError("Backup.slots.create is not implemented yet.")

    def disable(self) -> None:
        """Disable a backup slot."""
        raise NotImplementedError("Backup.slots.disable is not implemented yet.")

    def enable(self) -> None:
        """Enable a backup slot."""
        raise NotImplementedError("Backup.slots.enable is not implemented yet.")

    def display(self) -> None:
        """Get detailed information for a slot."""
        raise NotImplementedError("Backup.slots.display is not implemented yet.")

    def update(self) -> None:
        """Update slot attributes."""
        raise NotImplementedError("Backup.slots.update is not implemented yet.")

    def delete(self) -> None:
        """Delete a backup slot."""
        raise NotImplementedError("Backup.slots.delete is not implemented yet.")

    def rclone(self) -> None:
        """Retrieve rclone details for a backup slot."""
        raise NotImplementedError("Backup.slots.rclone is not implemented yet.")


class AsyncSlots(AsyncResource):
    """Async Swiss Backup slot management endpoints."""

    async def list(self) -> None:
        """List all backup slots."""
        raise NotImplementedError("AsyncBackup.slots.list is not implemented yet.")

    async def create(self) -> None:
        """Create a new backup slot."""
        raise NotImplementedError("AsyncBackup.slots.create is not implemented yet.")

    async def disable(self) -> None:
        """Disable a backup slot."""
        raise NotImplementedError("AsyncBackup.slots.disable is not implemented yet.")

    async def enable(self) -> None:
        """Enable a backup slot."""
        raise NotImplementedError("AsyncBackup.slots.enable is not implemented yet.")

    async def display(self) -> None:
        """Get detailed information for a slot."""
        raise NotImplementedError("AsyncBackup.slots.display is not implemented yet.")

    async def update(self) -> None:
        """Update slot attributes."""
        raise NotImplementedError("AsyncBackup.slots.update is not implemented yet.")

    async def delete(self) -> None:
        """Delete a backup slot."""
        raise NotImplementedError("AsyncBackup.slots.delete is not implemented yet.")

    async def rclone(self) -> None:
        """Retrieve rclone details for a backup slot."""
        raise NotImplementedError("AsyncBackup.slots.rclone is not implemented yet.")


__all__ = ["Slots", "AsyncSlots"]
