from infomaniak.resource import AsyncResource, Resouce


class Billing(Resouce):
    """Swiss Backup billing endpoints."""

    def list(self) -> None:
        """List prices and discounts for Swiss Backup plans."""
        raise NotImplementedError("Backup.billing.list is not implemented yet.")


class AsyncBilling(AsyncResource):
    """Async Swiss Backup billing endpoints."""

    async def list(self) -> None:
        """List prices and discounts for Swiss Backup plans."""
        raise NotImplementedError("AsyncBackup.billing.list is not implemented yet.")


__all__ = ["Billing", "AsyncBilling"]
