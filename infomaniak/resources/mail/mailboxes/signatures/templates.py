from infomaniak.resource import AsyncResource, Resouce


class Templates(Resouce):
    """Mailbox signature template endpoints."""

    def list(self) -> None:
        """List mailbox signature templates."""
        raise NotImplementedError("Mailbox signature templates list endpoint is not implemented yet.")

    def show(self) -> None:
        """Show a mailbox signature template."""
        raise NotImplementedError("Mailbox signature templates show endpoint is not implemented yet.")


class AsyncTemplates(AsyncResource):
    """Async mailbox signature template endpoints."""

    async def list(self) -> None:
        """List mailbox signature templates."""
        raise NotImplementedError("Mailbox signature templates list endpoint is not implemented yet.")

    async def show(self) -> None:
        """Show a mailbox signature template."""
        raise NotImplementedError("Mailbox signature templates show endpoint is not implemented yet.")


__all__ = ["Templates", "AsyncTemplates"]
