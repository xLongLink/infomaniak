from infomaniak.resource import AsyncResource, Resouce

from .thumbnail import AsyncTemplatesThumbnail, TemplatesThumbnail


class Templates(Resouce):
    """Newsletter templates endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.thumbnail = TemplatesThumbnail(client)

    def list(self) -> None:
        """List all templates."""
        raise NotImplementedError("Newsletter templates list endpoint is not implemented yet.")

    def display(self) -> None:
        """Show template HTML."""
        raise NotImplementedError("Newsletter templates display endpoint is not implemented yet.")

    def create_from_campaign(self) -> None:
        """Create a template from a campaign."""
        raise NotImplementedError(
            "Newsletter templates create_from_campaign endpoint is not implemented yet."
        )


class AsyncTemplates(AsyncResource):
    """Async newsletter templates endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.thumbnail = AsyncTemplatesThumbnail(client)

    async def list(self) -> None:
        """List all templates."""
        raise NotImplementedError("Newsletter templates list endpoint is not implemented yet.")

    async def display(self) -> None:
        """Show template HTML."""
        raise NotImplementedError("Newsletter templates display endpoint is not implemented yet.")

    async def create_from_campaign(self) -> None:
        """Create a template from a campaign."""
        raise NotImplementedError(
            "Newsletter templates create_from_campaign endpoint is not implemented yet."
        )


__all__ = ["Templates", "AsyncTemplates", "TemplatesThumbnail", "AsyncTemplatesThumbnail"]
