from infomaniak.resource import AsyncResource, Resouce

from .fields import AsyncWebformsFields, WebformsFields
from .themes import AsyncWebformsThemes, WebformsThemes


class Webforms(Resouce):
    """Newsletter webforms endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.themes = WebformsThemes(client)
        self.fields = WebformsFields(client)

    def list(self) -> None:
        """List all webforms."""
        raise NotImplementedError("Newsletter webforms list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a webform."""
        raise NotImplementedError("Newsletter webforms create endpoint is not implemented yet.")

    def delete_bulk(self) -> None:
        """Delete multiple webforms."""
        raise NotImplementedError("Newsletter webforms delete_bulk endpoint is not implemented yet.")

    def display(self) -> None:
        """Get a specific webform."""
        raise NotImplementedError("Newsletter webforms display endpoint is not implemented yet.")

    def update(self) -> None:
        """Update a webform."""
        raise NotImplementedError("Newsletter webforms update endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a webform."""
        raise NotImplementedError("Newsletter webforms delete endpoint is not implemented yet.")


class AsyncWebforms(AsyncResource):
    """Async newsletter webforms endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.themes = AsyncWebformsThemes(client)
        self.fields = AsyncWebformsFields(client)

    async def list(self) -> None:
        """List all webforms."""
        raise NotImplementedError("Newsletter webforms list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a webform."""
        raise NotImplementedError("Newsletter webforms create endpoint is not implemented yet.")

    async def delete_bulk(self) -> None:
        """Delete multiple webforms."""
        raise NotImplementedError("Newsletter webforms delete_bulk endpoint is not implemented yet.")

    async def display(self) -> None:
        """Get a specific webform."""
        raise NotImplementedError("Newsletter webforms display endpoint is not implemented yet.")

    async def update(self) -> None:
        """Update a webform."""
        raise NotImplementedError("Newsletter webforms update endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a webform."""
        raise NotImplementedError("Newsletter webforms delete endpoint is not implemented yet.")


__all__ = ["Webforms", "AsyncWebforms", "WebformsThemes", "AsyncWebformsThemes", "WebformsFields", "AsyncWebformsFields"]
