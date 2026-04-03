from infomaniak.resource import AsyncResource, Resouce


class StatsViewing(Resouce):
    """Video statistics viewing endpoints."""

    def time(self) -> None:
        raise NotImplementedError("Video.stats.*.viewing.time is not implemented yet.")

    def histogram_per_channel(self) -> None:
        raise NotImplementedError("Video.stats.*.viewing.histogram_per_channel is not implemented yet.")


class AsyncStatsViewing(AsyncResource):
    """Async video statistics viewing endpoints."""

    async def time(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.*.viewing.time is not implemented yet.")

    async def histogram_per_channel(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.*.viewing.histogram_per_channel is not implemented yet.")
