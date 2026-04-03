from infomaniak.resource import AsyncResource, Resouce

from .campaigns import AsyncCampaigns, Campaigns
from .credits import AsyncCredits, Credits
from .dashboard import AsyncDashboard, Dashboard
from .domains import AsyncDomains, Domains
from .fields import AsyncFields, Fields
from .groups import AsyncGroups, Groups
from .operations import AsyncOperations, Operations
from .segments import AsyncSegments, Segments
from .subscribers import AsyncSubscribers, Subscribers
from .templates import AsyncTemplates, Templates
from .webforms import AsyncWebforms, Webforms


class Newsletter(Resouce):
    """Newsletter resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.campaigns = Campaigns(client)
        self.credits = Credits(client)
        self.dashboard = Dashboard(client)
        self.domains = Domains(client)
        self.fields = Fields(client)
        self.groups = Groups(client)
        self.operations = Operations(client)
        self.segments = Segments(client)
        self.subscribers = Subscribers(client)
        self.templates = Templates(client)
        self.webforms = Webforms(client)


class AsyncNewsletter(AsyncResource):
    """Async newsletter resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.campaigns = AsyncCampaigns(client)
        self.credits = AsyncCredits(client)
        self.dashboard = AsyncDashboard(client)
        self.domains = AsyncDomains(client)
        self.fields = AsyncFields(client)
        self.groups = AsyncGroups(client)
        self.operations = AsyncOperations(client)
        self.segments = AsyncSegments(client)
        self.subscribers = AsyncSubscribers(client)
        self.templates = AsyncTemplates(client)
        self.webforms = AsyncWebforms(client)


__all__ = [
    "Newsletter",
    "AsyncNewsletter",
    "Campaigns",
    "AsyncCampaigns",
    "Credits",
    "AsyncCredits",
    "Dashboard",
    "AsyncDashboard",
    "Domains",
    "AsyncDomains",
    "Fields",
    "AsyncFields",
    "Groups",
    "AsyncGroups",
    "Operations",
    "AsyncOperations",
    "Segments",
    "AsyncSegments",
    "Subscribers",
    "AsyncSubscribers",
    "Templates",
    "AsyncTemplates",
    "Webforms",
    "AsyncWebforms",
]
