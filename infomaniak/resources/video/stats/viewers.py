from infomaniak.resource import AsyncResource, Resouce


class StatsViewers(Resouce):
    """Video statistics viewers endpoints."""

    def list(self) -> None:
        raise NotImplementedError("Video.stats.*.viewers.list is not implemented yet.")

    def unique(self) -> None:
        raise NotImplementedError("Video.stats.*.viewers.unique is not implemented yet.")

    def histogram(self) -> None:
        raise NotImplementedError("Video.stats.*.viewers.histogram is not implemented yet.")

    def histogram_per_channel(self) -> None:
        raise NotImplementedError("Video.stats.*.viewers.histogram_per_channel is not implemented yet.")

    def share(self) -> None:
        raise NotImplementedError("Video.stats.*.viewers.share is not implemented yet.")


class AsyncStatsViewers(AsyncResource):
    """Async video statistics viewers endpoints."""

    async def list(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.*.viewers.list is not implemented yet.")

    async def unique(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.*.viewers.unique is not implemented yet.")

    async def histogram(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.*.viewers.histogram is not implemented yet.")

    async def histogram_per_channel(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.*.viewers.histogram_per_channel is not implemented yet.")

    async def share(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.*.viewers.share is not implemented yet.")
