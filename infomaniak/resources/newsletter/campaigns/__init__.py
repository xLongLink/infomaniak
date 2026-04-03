from infomaniak.resource import AsyncResource, Resouce

from .template import AsyncCampaignsTemplate, CampaignsTemplate


class Campaigns(Resouce):
    """Newsletter campaigns endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.template = CampaignsTemplate(client)

    def list(self) -> None:
        """List all campaigns."""
        raise NotImplementedError("Newsletter campaigns list endpoint is not implemented yet.")

    def create(self) -> None:
        """Create a campaign."""
        raise NotImplementedError("Newsletter campaigns create endpoint is not implemented yet.")

    def delete_bulk(self) -> None:
        """Bulk delete campaigns."""
        raise NotImplementedError("Newsletter campaigns delete_bulk endpoint is not implemented yet.")

    def display(self) -> None:
        """Retrieve a single campaign."""
        raise NotImplementedError("Newsletter campaigns display endpoint is not implemented yet.")

    def update(self) -> None:
        """Edit a campaign."""
        raise NotImplementedError("Newsletter campaigns update endpoint is not implemented yet.")

    def delete(self) -> None:
        """Delete a campaign."""
        raise NotImplementedError("Newsletter campaigns delete endpoint is not implemented yet.")

    def tracking(self) -> None:
        """Get campaign tracking information."""
        raise NotImplementedError("Newsletter campaigns tracking endpoint is not implemented yet.")

    def links_activity(self) -> None:
        """Get link-click statistics for a campaign."""
        raise NotImplementedError("Newsletter campaigns links_activity endpoint is not implemented yet.")

    def subscribers_activity(self) -> None:
        """Get subscriber activity for a campaign."""
        raise NotImplementedError(
            "Newsletter campaigns subscribers_activity endpoint is not implemented yet."
        )

    def test(self) -> None:
        """Send a test of a specific campaign."""
        raise NotImplementedError("Newsletter campaigns test endpoint is not implemented yet.")

    def duplicate(self) -> None:
        """Duplicate a campaign."""
        raise NotImplementedError("Newsletter campaigns duplicate endpoint is not implemented yet.")

    def cancel(self) -> None:
        """Cancel a scheduled campaign."""
        raise NotImplementedError("Newsletter campaigns cancel endpoint is not implemented yet.")

    def schedule(self) -> None:
        """Schedule a campaign."""
        raise NotImplementedError("Newsletter campaigns schedule endpoint is not implemented yet.")


class AsyncCampaigns(AsyncResource):
    """Async newsletter campaigns endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.template = AsyncCampaignsTemplate(client)

    async def list(self) -> None:
        """List all campaigns."""
        raise NotImplementedError("Newsletter campaigns list endpoint is not implemented yet.")

    async def create(self) -> None:
        """Create a campaign."""
        raise NotImplementedError("Newsletter campaigns create endpoint is not implemented yet.")

    async def delete_bulk(self) -> None:
        """Bulk delete campaigns."""
        raise NotImplementedError("Newsletter campaigns delete_bulk endpoint is not implemented yet.")

    async def display(self) -> None:
        """Retrieve a single campaign."""
        raise NotImplementedError("Newsletter campaigns display endpoint is not implemented yet.")

    async def update(self) -> None:
        """Edit a campaign."""
        raise NotImplementedError("Newsletter campaigns update endpoint is not implemented yet.")

    async def delete(self) -> None:
        """Delete a campaign."""
        raise NotImplementedError("Newsletter campaigns delete endpoint is not implemented yet.")

    async def tracking(self) -> None:
        """Get campaign tracking information."""
        raise NotImplementedError("Newsletter campaigns tracking endpoint is not implemented yet.")

    async def links_activity(self) -> None:
        """Get link-click statistics for a campaign."""
        raise NotImplementedError("Newsletter campaigns links_activity endpoint is not implemented yet.")

    async def subscribers_activity(self) -> None:
        """Get subscriber activity for a campaign."""
        raise NotImplementedError(
            "Newsletter campaigns subscribers_activity endpoint is not implemented yet."
        )

    async def test(self) -> None:
        """Send a test of a specific campaign."""
        raise NotImplementedError("Newsletter campaigns test endpoint is not implemented yet.")

    async def duplicate(self) -> None:
        """Duplicate a campaign."""
        raise NotImplementedError("Newsletter campaigns duplicate endpoint is not implemented yet.")

    async def cancel(self) -> None:
        """Cancel a scheduled campaign."""
        raise NotImplementedError("Newsletter campaigns cancel endpoint is not implemented yet.")

    async def schedule(self) -> None:
        """Schedule a campaign."""
        raise NotImplementedError("Newsletter campaigns schedule endpoint is not implemented yet.")


__all__ = ["Campaigns", "AsyncCampaigns", "CampaignsTemplate", "AsyncCampaignsTemplate"]
