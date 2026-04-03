from infomaniak.resource import AsyncResource, Resouce

from .geolocation import AsyncStatsGeolocation, StatsGeolocation
from .viewers import AsyncStatsViewers, StatsViewers
from .viewing import AsyncStatsViewing, StatsViewing


class GlobalStats(Resouce):
    """Global video statistics endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.geolocation = StatsGeolocation(client)
        self.viewers = StatsViewers(client)
        self.viewing = StatsViewing(client)

    def consumption(self) -> None:
        raise NotImplementedError("Video.stats.globals.consumption is not implemented yet.")

    def consumption_histogram(self) -> None:
        raise NotImplementedError("Video.stats.globals.consumption_histogram is not implemented yet.")


class AsyncGlobalStats(AsyncResource):
    """Async global video statistics endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.geolocation = AsyncStatsGeolocation(client)
        self.viewers = AsyncStatsViewers(client)
        self.viewing = AsyncStatsViewing(client)

    async def consumption(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.globals.consumption is not implemented yet.")

    async def consumption_histogram(self) -> None:
        raise NotImplementedError("AsyncVideo.stats.globals.consumption_histogram is not implemented yet.")
