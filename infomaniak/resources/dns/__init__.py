from infomaniak.resource import AsyncResource, Resouce

from .domain import AsyncDomain, Domain
from .tld import AsyncTLD, TLD
from .zone import AsyncZone, Zone


class DNS(Resouce):
    """DNS resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.domain = Domain(client)
        self.tld = TLD(client)
        self.zone = Zone(client)


class AsyncDNS(AsyncResource):
    """Async DNS resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.domain = AsyncDomain(client)
        self.tld = AsyncTLD(client)
        self.zone = AsyncZone(client)


__all__ = [
    "DNS",
    "AsyncDNS",
    "Domain",
    "AsyncDomain",
    "TLD",
    "AsyncTLD",
    "Zone",
    "AsyncZone",
]
