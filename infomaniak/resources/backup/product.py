from infomaniak.resource import AsyncResource, Resouce


class Product(Resouce):
    """Swiss Backup product management endpoints."""

    def list(self) -> None:
        """List all Swiss Backup products available for the account."""
        raise NotImplementedError("Backup.product.list is not implemented yet.")

    def display(self) -> None:
        """Show details for a specific Swiss Backup product."""
        raise NotImplementedError("Backup.product.display is not implemented yet.")

    def update(self) -> None:
        """Update a Swiss Backup product."""
        raise NotImplementedError("Backup.product.update is not implemented yet.")

    def acronis(self) -> None:
        """Retrieve Acronis-specific details for a Swiss Backup product."""
        raise NotImplementedError("Backup.product.acronis is not implemented yet.")


class AsyncProduct(AsyncResource):
    """Async Swiss Backup product management endpoints."""

    async def list(self) -> None:
        """List all Swiss Backup products available for the account."""
        raise NotImplementedError("AsyncBackup.product.list is not implemented yet.")

    async def display(self) -> None:
        """Show details for a specific Swiss Backup product."""
        raise NotImplementedError("AsyncBackup.product.display is not implemented yet.")

    async def update(self) -> None:
        """Update a Swiss Backup product."""
        raise NotImplementedError("AsyncBackup.product.update is not implemented yet.")

    async def acronis(self) -> None:
        """Retrieve Acronis-specific details for a Swiss Backup product."""
        raise NotImplementedError("AsyncBackup.product.acronis is not implemented yet.")


__all__ = ["Product", "AsyncProduct"]
