from infomaniak.resource import AsyncResource, Resouce


class AutoReply(Resouce):
    """Mailbox auto-reply endpoints."""

    def list_models(self) -> None:
        """List auto-reply models for a mailbox."""
        raise NotImplementedError("Mailbox auto-reply list_models endpoint is not implemented yet.")

    def add_model(self) -> None:
        """Add an auto-reply model for a mailbox."""
        raise NotImplementedError("Mailbox auto-reply add_model endpoint is not implemented yet.")

    def reset(self) -> None:
        """Reset auto-reply counters for a mailbox."""
        raise NotImplementedError("Mailbox auto-reply reset endpoint is not implemented yet.")

    def show_model(self) -> None:
        """Show an auto-reply model for a mailbox."""
        raise NotImplementedError("Mailbox auto-reply show_model endpoint is not implemented yet.")

    def delete_model(self) -> None:
        """Delete an auto-reply model for a mailbox."""
        raise NotImplementedError("Mailbox auto-reply delete_model endpoint is not implemented yet.")

    def update_model(self) -> None:
        """Update an auto-reply model for a mailbox."""
        raise NotImplementedError("Mailbox auto-reply update_model endpoint is not implemented yet.")


class AsyncAutoReply(AsyncResource):
    """Async mailbox auto-reply endpoints."""

    async def list_models(self) -> None:
        """List auto-reply models for a mailbox."""
        raise NotImplementedError("Mailbox auto-reply list_models endpoint is not implemented yet.")

    async def add_model(self) -> None:
        """Add an auto-reply model for a mailbox."""
        raise NotImplementedError("Mailbox auto-reply add_model endpoint is not implemented yet.")

    async def reset(self) -> None:
        """Reset auto-reply counters for a mailbox."""
        raise NotImplementedError("Mailbox auto-reply reset endpoint is not implemented yet.")

    async def show_model(self) -> None:
        """Show an auto-reply model for a mailbox."""
        raise NotImplementedError("Mailbox auto-reply show_model endpoint is not implemented yet.")

    async def delete_model(self) -> None:
        """Delete an auto-reply model for a mailbox."""
        raise NotImplementedError("Mailbox auto-reply delete_model endpoint is not implemented yet.")

    async def update_model(self) -> None:
        """Update an auto-reply model for a mailbox."""
        raise NotImplementedError("Mailbox auto-reply update_model endpoint is not implemented yet.")


__all__ = ["AutoReply", "AsyncAutoReply"]
