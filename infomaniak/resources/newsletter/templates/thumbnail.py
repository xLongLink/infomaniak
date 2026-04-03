from infomaniak.resource import AsyncResource, Resouce


class TemplatesThumbnail(Resouce):
    """Newsletter template thumbnail endpoints."""

    def update(self) -> None:
        """Update a template thumbnail."""
        raise NotImplementedError(
            "Newsletter templates thumbnail update endpoint is not implemented yet."
        )


class AsyncTemplatesThumbnail(AsyncResource):
    """Async newsletter template thumbnail endpoints."""

    async def update(self) -> None:
        """Update a template thumbnail."""
        raise NotImplementedError(
            "Newsletter templates thumbnail update endpoint is not implemented yet."
        )


__all__ = ["TemplatesThumbnail", "AsyncTemplatesThumbnail"]
