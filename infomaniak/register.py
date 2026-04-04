from infomaniak.clients import AsyncBaseClient, BaseClient

# Load and connect resources to the clients
from infomaniak.resources.backup import AsyncBackup, Backup
from infomaniak.resources.cloud import AsyncCloud, Cloud
from infomaniak.resources.core import AsyncCore, Core
from infomaniak.resources.dns import AsyncDNS, DNS
from infomaniak.resources.domain import AsyncDomain, Domain
from infomaniak.resources.etickets import AsyncEtickets, Etickets
from infomaniak.resources.kchat import AsyncKchat, Kchat
from infomaniak.resources.kdrive import AsyncKdrive, Kdrive
from infomaniak.resources.kmeet import AsyncKmeet, Kmeet
from infomaniak.resources.mail import AsyncMail, Mail
from infomaniak.resources.newsletter import AsyncNewsletter, Newsletter
from infomaniak.resources.radio import AsyncRadio, Radio
from infomaniak.resources.url import AsyncUrl, Url
from infomaniak.resources.video import AsyncVideo, Video


class Client(BaseClient):
    """Sync resource-based SDK client."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.backup = Backup(self)
        self.cloud = Cloud(self)
        self.core = Core(self)
        self.dns = DNS(self)
        self.domain = Domain(self)
        self.etickets = Etickets(self)
        self.kchat = Kchat(self)
        self.kdrive = Kdrive(self)
        self.kmeet = Kmeet(self)
        self.mail = Mail(self)
        self.newsletter = Newsletter(self)
        self.radio = Radio(self)
        self.url = Url(self)
        self.video = Video(self)


class AsyncClient(AsyncBaseClient):
    """Async resource-based SDK client."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.backup = AsyncBackup(self)
        self.cloud = AsyncCloud(self)
        self.core = AsyncCore(self)
        self.dns = AsyncDNS(self)
        self.domain = AsyncDomain(self)
        self.etickets = AsyncEtickets(self)
        self.kchat = AsyncKchat(self)
        self.kdrive = AsyncKdrive(self)
        self.kmeet = AsyncKmeet(self)
        self.mail = AsyncMail(self)
        self.newsletter = AsyncNewsletter(self)
        self.radio = AsyncRadio(self)
        self.url = AsyncUrl(self)
        self.video = AsyncVideo(self)
