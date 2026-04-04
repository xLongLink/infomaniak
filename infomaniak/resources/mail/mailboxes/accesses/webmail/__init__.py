from infomaniak.resource import AsyncResource, Resouce

from .team import AsyncTeam, Team
from .user import AsyncUser, User


class Webmail(Resouce):
    """Mailbox webmail access nested resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.team = Team(client)
        self.user = User(client)


class AsyncWebmail(AsyncResource):
    """Async mailbox webmail access nested resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.team = AsyncTeam(client)
        self.user = AsyncUser(client)


__all__ = ["Webmail", "AsyncWebmail", "Team", "AsyncTeam", "User", "AsyncUser"]
