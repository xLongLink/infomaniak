from infomaniak.resource import AsyncResource, Resouce

from .devices import AsyncDevices, Devices
from .invitations import AsyncInvitations, Invitations
from .webmail import AsyncWebmail, Webmail


class Accesses(Resouce):
    """Mailbox accesses nested resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.devices = Devices(client)
        self.invitations = Invitations(client)
        self.webmail = Webmail(client)


class AsyncAccesses(AsyncResource):
    """Async mailbox accesses nested resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.devices = AsyncDevices(client)
        self.invitations = AsyncInvitations(client)
        self.webmail = AsyncWebmail(client)


__all__ = [
    "Accesses",
    "AsyncAccesses",
    "Devices",
    "AsyncDevices",
    "Invitations",
    "AsyncInvitations",
    "Webmail",
    "AsyncWebmail",
]
