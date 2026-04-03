from infomaniak.resource import AsyncResource, Resouce

from .actions import Actions, AsyncActions
from .countries import AsyncCountries, Countries
from .events import AsyncEvents, Events
from .ksuite import AsyncKsuite, Ksuite
from .languages import AsyncLanguages, Languages
from .products import AsyncProducts, Products
from .profile import AsyncProfile, Profile
from .tasks import AsyncTasks, Tasks
from .timezones import AsyncTimezones, Timezones
from .user import AsyncUser, User


class Core(Resouce):
    """Core resources for Infomaniak services."""

    def __init__(self, client):
        super().__init__(client)
        self.actions = Actions(client)
        self.countries = Countries(client)
        self.events = Events(client)
        self.ksuite = Ksuite(client)
        self.languages = Languages(client)
        self.products = Products(client)
        self.profile = Profile(client)
        self.tasks = Tasks(client)
        self.timezones = Timezones(client)
        self.user = User(client)


class AsyncCore(AsyncResource):
    """Async core resources for Infomaniak services."""

    def __init__(self, client):
        super().__init__(client)
        self.actions = AsyncActions(client)
        self.countries = AsyncCountries(client)
        self.events = AsyncEvents(client)
        self.ksuite = AsyncKsuite(client)
        self.languages = AsyncLanguages(client)
        self.products = AsyncProducts(client)
        self.profile = AsyncProfile(client)
        self.tasks = AsyncTasks(client)
        self.timezones = AsyncTimezones(client)
        self.user = AsyncUser(client)
