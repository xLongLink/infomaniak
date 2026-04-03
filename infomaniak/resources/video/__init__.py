from infomaniak.resource import AsyncResource, Resouce

from .channel import AsyncChannel, Channel
from .countries import AsyncCountries, Countries
from .event import AsyncEvent, Event
from .integrations import AsyncIntegrations, Integrations
from .live import AsyncLive, Live
from .options import AsyncOptions, Options
from .order import AsyncOrder, Order
from .players import AsyncPlayers, Players
from .prices import AsyncPrices, Prices
from .restrictions import AsyncRestrictions, Restrictions
from .stats import AsyncStats, Stats
from .stream import AsyncStream, Stream
from .thumbnail import AsyncThumbnail, Thumbnail
from .timezones import AsyncTimezones, Timezones


class Video(Resouce):
    """Video resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.channel = Channel(client)
        self.countries = Countries(client)
        self.event = Event(client)
        self.integrations = Integrations(client)
        self.live = Live(client)
        self.options = Options(client)
        self.order = Order(client)
        self.players = Players(client)
        self.prices = Prices(client)
        self.restrictions = Restrictions(client)
        self.stats = Stats(client)
        self.stream = Stream(client)
        self.thumbnail = Thumbnail(client)
        self.timezones = Timezones(client)


class AsyncVideo(AsyncResource):
    """Async video resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.channel = AsyncChannel(client)
        self.countries = AsyncCountries(client)
        self.event = AsyncEvent(client)
        self.integrations = AsyncIntegrations(client)
        self.live = AsyncLive(client)
        self.options = AsyncOptions(client)
        self.order = AsyncOrder(client)
        self.players = AsyncPlayers(client)
        self.prices = AsyncPrices(client)
        self.restrictions = AsyncRestrictions(client)
        self.stats = AsyncStats(client)
        self.stream = AsyncStream(client)
        self.thumbnail = AsyncThumbnail(client)
        self.timezones = AsyncTimezones(client)


__all__ = [
    "Video",
    "AsyncVideo",
    "Channel",
    "AsyncChannel",
    "Countries",
    "AsyncCountries",
    "Event",
    "AsyncEvent",
    "Integrations",
    "AsyncIntegrations",
    "Live",
    "AsyncLive",
    "Options",
    "AsyncOptions",
    "Order",
    "AsyncOrder",
    "Players",
    "AsyncPlayers",
    "Prices",
    "AsyncPrices",
    "Restrictions",
    "AsyncRestrictions",
    "Stats",
    "AsyncStats",
    "Stream",
    "AsyncStream",
    "Thumbnail",
    "AsyncThumbnail",
    "Timezones",
    "AsyncTimezones",
]
