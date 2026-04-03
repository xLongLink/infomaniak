from infomaniak.resource import AsyncResource, Resouce

from .channel import AsyncChannelStats, ChannelStats
from .globals_ import AsyncGlobalStats, GlobalStats


class Stats(Resouce):
    """Video statistics endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.channel = ChannelStats(client)
        self.globals = GlobalStats(client)


class AsyncStats(AsyncResource):
    """Async video statistics endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.channel = AsyncChannelStats(client)
        self.globals = AsyncGlobalStats(client)


__all__ = ["Stats", "AsyncStats", "ChannelStats", "AsyncChannelStats", "GlobalStats", "AsyncGlobalStats"]
