from infomaniak.resource import AsyncResource, Resouce


class WebformsThemes(Resouce):
    """Newsletter webforms themes endpoints."""

    def list(self) -> None:
        """List available webform themes."""
        raise NotImplementedError(
            "Newsletter webforms themes list endpoint is not implemented yet."
        )


class AsyncWebformsThemes(AsyncResource):
    """Async newsletter webforms themes endpoints."""

    async def list(self) -> None:
        """List available webform themes."""
        raise NotImplementedError(
            "Newsletter webforms themes list endpoint is not implemented yet."
        )


__all__ = ["WebformsThemes", "AsyncWebformsThemes"]
