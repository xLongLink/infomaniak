from infomaniak.resource import AsyncResource, Resouce

from .accesses import Accesses, AsyncAccesses
from .aliases import Aliases, AsyncAliases
from .auto_reply import AsyncAutoReply, AutoReply
from .filters import AsyncFilters, Filters
from .folders import AsyncFolders, Folders
from .forwarding import AsyncForwarding, Forwarding
from .signatures import AsyncSignatures, Signatures
from .users import AsyncUsers, Users


class Mailboxes(Resouce):
    """Mailboxes nested resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.accesses = Accesses(client)
        self.aliases = Aliases(client)
        self.auto_reply = AutoReply(client)
        self.filters = Filters(client)
        self.folders = Folders(client)
        self.forwarding = Forwarding(client)
        self.signatures = Signatures(client)
        self.users = Users(client)


class AsyncMailboxes(AsyncResource):
    """Async mailboxes nested resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.accesses = AsyncAccesses(client)
        self.aliases = AsyncAliases(client)
        self.auto_reply = AsyncAutoReply(client)
        self.filters = AsyncFilters(client)
        self.folders = AsyncFolders(client)
        self.forwarding = AsyncForwarding(client)
        self.signatures = AsyncSignatures(client)
        self.users = AsyncUsers(client)


__all__ = [
    "Mailboxes",
    "AsyncMailboxes",
    "Accesses",
    "AsyncAccesses",
    "Aliases",
    "AsyncAliases",
    "AutoReply",
    "AsyncAutoReply",
    "Filters",
    "AsyncFilters",
    "Folders",
    "AsyncFolders",
    "Forwarding",
    "AsyncForwarding",
    "Signatures",
    "AsyncSignatures",
    "Users",
    "AsyncUsers",
]
