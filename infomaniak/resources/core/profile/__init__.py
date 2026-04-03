from infomaniak.resource import AsyncResource, Resouce

from .avatar import AsyncProfileAvatar, ProfileAvatar
from .email import AsyncProfileEmail, ProfileEmail
from .info import AsyncProfileInfo, ProfileInfo
from .password import AsyncProfilePassword, ProfilePassword
from .phone import AsyncProfilePhone, ProfilePhone


class Profile(Resouce):
    """Core profile endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.password = ProfilePassword(client)
        self.email = ProfileEmail(client)
        self.phone = ProfilePhone(client)
        self.avatar = ProfileAvatar(client)
        self.info = ProfileInfo(client)


class AsyncProfile(AsyncResource):
    """Async core profile endpoints."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.password = AsyncProfilePassword(client)
        self.email = AsyncProfileEmail(client)
        self.phone = AsyncProfilePhone(client)
        self.avatar = AsyncProfileAvatar(client)
        self.info = AsyncProfileInfo(client)
