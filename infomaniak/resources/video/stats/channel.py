from infomaniak.resource import AsyncResource, Resouce

from .geolocation import AsyncStatsGeolocation, StatsGeolocation
from .viewers import AsyncStatsViewers, StatsViewers
from .viewing import AsyncStatsViewing, StatsViewing


class ChannelStats(Resouce):
    """Per-channel video statistics endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.geolocation = StatsGeolocation(client)
        self.viewers = StatsViewers(client)
        self.viewing = StatsViewing(client)

    def consumption(self) -> None:
        raise NotImplementedError("Video.stats.channel.consumption is not implemented yet.")

    def consumption_histogram(self) -> None:
        raise NotImplementedError("Video.stats.channel.consumption_histogram is not implemented yet.")


class AsyncChannelStats(AsyncResource):
    """Async per-channel video statistics endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.geolocation = AsyncStatsGeolocation(client)
        self.viewers = AsyncStatsViewers(client)
        self.viewing = AsyncStatsViewing(client)

    async def consumption(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.channel.consumption is not implemented yet.")

    async def consumption_histogram(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.channel.consumption_histogram is not implemented yet.")
