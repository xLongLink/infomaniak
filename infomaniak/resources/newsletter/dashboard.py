from infomaniak.resource import AsyncResource, Resouce


class Dashboard(Resouce):
    """Newsletter dashboard endpoints."""

    def display(self) -> None:
        """Show dashboard information."""
        raise NotImplementedError("Newsletter dashboard display endpoint is not implemented yet.")

    def latest_campaigns(self) -> None:
        """List latest campaigns."""
        raise NotImplementedError(
            "Newsletter dashboard latest_campaigns endpoint is not implemented yet."
        )

    def subscribers_statistics(self) -> None:
        """List subscriber statistics."""
        raise NotImplementedError(
            "Newsletter dashboard subscribers_statistics endpoint is not implemented yet."
        )

    def campaigns_statistics(self) -> None:
        """List campaign statistics."""
        raise NotImplementedError(
            "Newsletter dashboard campaigns_statistics endpoint is not implemented yet."
        )

    def monthly_campaigns_statistics(self) -> None:
        """List monthly campaign statistics."""
        raise NotImplementedError(
            "Newsletter dashboard monthly_campaigns_statistics endpoint is not implemented yet."
        )


class AsyncDashboard(AsyncResource):
    """Async newsletter dashboard endpoints."""

    async def display(self) -> None:
        """Show dashboard information."""
        raise NotImplementedError("Newsletter dashboard display endpoint is not implemented yet.")

    async def latest_campaigns(self) -> None:
        """List latest campaigns."""
        raise NotImplementedError(
            "Newsletter dashboard latest_campaigns endpoint is not implemented yet."
        )

    async def subscribers_statistics(self) -> None:
        """List subscriber statistics."""
        raise NotImplementedError(
            "Newsletter dashboard subscribers_statistics endpoint is not implemented yet."
        )

    async def campaigns_statistics(self) -> None:
        """List campaign statistics."""
        raise NotImplementedError(
            "Newsletter dashboard campaigns_statistics endpoint is not implemented yet."
        )

    async def monthly_campaigns_statistics(self) -> None:
        """List monthly campaign statistics."""
        raise NotImplementedError(
            "Newsletter dashboard monthly_campaigns_statistics endpoint is not implemented yet."
        )


__all__ = ["Dashboard", "AsyncDashboard"]
