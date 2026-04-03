from infomaniak.resource import AsyncResource, Resouce

from .plan import AsyncPlan, Plan
from .room import AsyncRoom, Room


class Kmeet(Resouce):
    """kMeet resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.plan = Plan(client)
        self.room = Room(client)


class AsyncKmeet(AsyncResource):
    """Async kMeet resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.plan = AsyncPlan(client)
        self.room = AsyncRoom(client)


__all__ = [
    "Kmeet",
    "AsyncKmeet",
    "Plan",
    "AsyncPlan",
    "Room",
    "AsyncRoom",
]
