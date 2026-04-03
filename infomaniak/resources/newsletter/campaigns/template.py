from infomaniak.resource import AsyncResource, Resouce


class CampaignsTemplate(Resouce):
    """Newsletter campaign template endpoints."""

    def test(self) -> None:
        """Send a test using a campaign template."""
        raise NotImplementedError(
            "Newsletter campaigns template test endpoint is not implemented yet."
        )


class AsyncCampaignsTemplate(AsyncResource):
    """Async newsletter campaign template endpoints."""

    async def test(self) -> None:
        """Send a test using a campaign template."""
        raise NotImplementedError(
            "Newsletter campaigns template test endpoint is not implemented yet."
        )


__all__ = ["CampaignsTemplate", "AsyncCampaignsTemplate"]
