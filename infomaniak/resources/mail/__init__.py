from infomaniak.resource import AsyncResource, Resouce

from .mailbox_management import AsyncMailboxManagement, MailboxManagement
from .mailboxes import AsyncMailboxes, Mailboxes


class Mail(Resouce):
    """Mail resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.mailbox_management = MailboxManagement(client)
        self.mailboxes = Mailboxes(client)


class AsyncMail(AsyncResource):
    """Async mail resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.mailbox_management = AsyncMailboxManagement(client)
        self.mailboxes = AsyncMailboxes(client)


__all__ = [
    "Mail",
    "AsyncMail",
    "MailboxManagement",
    "AsyncMailboxManagement",
    "Mailboxes",
    "AsyncMailboxes",
]
