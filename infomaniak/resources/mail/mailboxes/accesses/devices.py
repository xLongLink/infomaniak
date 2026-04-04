from infomaniak.resource import AsyncResource, Resouce


class Devices(Resouce):
    """Mailbox device access endpoints."""

    def list(self) -> None:
        """List device accesses for a mailbox."""
        raise NotImplementedError("Mailbox devices list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a device access."""
        raise NotImplementedError("Mailbox devices create endpoint is not implemented yet.")

    def delete_all(self) -> None:
        """Delete all device accesses for a mailbox."""
        raise NotImplementedError("Mailbox devices delete_all endpoint is not implemented yet.")

    def update_password(self) -> None:
        """Update a device access password."""
        raise NotImplementedError("Mailbox devices update_password endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a single device access."""
        raise NotImplementedError("Mailbox devices delete endpoint is not implemented yet.")

    def list_for_user(self) -> None:
        """List device accesses for a given user."""
        raise NotImplementedError("Mailbox devices list_for_user endpoint is not implemented yet.")

    def delete_for_user(self) -> None:
        """Delete a device access for a given user."""
        raise NotImplementedError("Mailbox devices delete_for_user endpoint is not implemented yet.")

    def list_by_user(self) -> None:
        """List devices by user."""
        raise NotImplementedError("Mailbox devices list_by_user endpoint is not implemented yet.")

    def list_by_device(self) -> None:
        """List a device."""
        raise NotImplementedError("Mailbox devices list_by_device endpoint is not implemented yet.")

    def delete_for_current_user(self) -> None:
        """Delete all device accesses for current user."""
        raise NotImplementedError("Mailbox devices delete_for_current_user endpoint is not implemented yet.")

    def delete_for_device(self) -> None:
        """Delete device accesses for a device."""
        raise NotImplementedError("Mailbox devices delete_for_device endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a device access."""
        raise NotImplementedError("Mailbox devices update endpoint is not implemented yet.")


class AsyncDevices(AsyncResource):
    """Async mailbox device access endpoints."""

    async def list(self) -> None:
        """List device accesses for a mailbox."""
        raise NotImplementedError("Mailbox devices list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a device access."""
        raise NotImplementedError("Mailbox devices create endpoint is not implemented yet.")

    async def delete_all(self) -> None:
        """Delete all device accesses for a mailbox."""
        raise NotImplementedError("Mailbox devices delete_all endpoint is not implemented yet.")

    async def update_password(self) -> None:
        """Update a device access password."""
        raise NotImplementedError("Mailbox devices update_password endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a single device access."""
        raise NotImplementedError("Mailbox devices delete endpoint is not implemented yet.")

    async def list_for_user(self) -> None:
        """List device accesses for a given user."""
        raise NotImplementedError("Mailbox devices list_for_user endpoint is not implemented yet.")

    async def delete_for_user(self) -> None:
        """Delete a device access for a given user."""
        raise NotImplementedError("Mailbox devices delete_for_user endpoint is not implemented yet.")

    async def list_by_user(self) -> None:
        """List devices by user."""
        raise NotImplementedError("Mailbox devices list_by_user endpoint is not implemented yet.")

    async def list_by_device(self) -> None:
        """List a device."""
        raise NotImplementedError("Mailbox devices list_by_device endpoint is not implemented yet.")

    async def delete_for_current_user(self) -> None:
        """Delete all device accesses for current user."""
        raise NotImplementedError("Mailbox devices delete_for_current_user endpoint is not implemented yet.")

    async def delete_for_device(self) -> None:
        """Delete device accesses for a device."""
        raise NotImplementedError("Mailbox devices delete_for_device endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a device access."""
        raise NotImplementedError("Mailbox devices update endpoint is not implemented yet.")


__all__ = ["Devices", "AsyncDevices"]
