from infomaniak.resource import AsyncResource, Resouce

from .administrator import Administrator, AsyncAdministrator
from .billing import AsyncBilling, Billing
from .passwords import AsyncPasswords, Passwords
from .product import AsyncProduct, Product
from .slots import AsyncSlots, Slots


class Backup(Resouce):
    """Swiss Backup resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.product = Product(client)
        self.slots = Slots(client)
        self.administrator = Administrator(client)
        self.passwords = Passwords(client)
        self.billing = Billing(client)


class AsyncBackup(AsyncResource):
    """Async Swiss Backup resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.product = AsyncProduct(client)
        self.slots = AsyncSlots(client)
        self.administrator = AsyncAdministrator(client)
        self.passwords = AsyncPasswords(client)
        self.billing = AsyncBilling(client)


__all__ = [
    "Backup",
    "AsyncBackup",
    "Product",
    "AsyncProduct",
    "Slots",
    "AsyncSlots",
    "Administrator",
    "AsyncAdministrator",
    "Passwords",
    "AsyncPasswords",
    "Billing",
    "AsyncBilling",
]
