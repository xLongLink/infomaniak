from infomaniak.clients import BaseClient, AsyncBaseClient
from infomaniak.resources.dns import DNS, AsyncDNS
from infomaniak.resources.url import Url, AsyncUrl
from infomaniak.resources.core import Core, AsyncCore
from infomaniak.resources.mail import Mail, AsyncMail
from infomaniak.resources.cloud import Cloud, AsyncCloud
from infomaniak.resources.kchat import Kchat, AsyncKchat
from infomaniak.resources.kmeet import Kmeet, AsyncKmeet
from infomaniak.resources.radio import Radio, AsyncRadio
from infomaniak.resources.tasks import Tasks, AsyncTasks
from infomaniak.resources.video import Video, AsyncVideo
# Load and connect resources to the clients
from infomaniak.resources.backup import Backup, AsyncBackup
from infomaniak.resources.domain import Domain, AsyncDomain
from infomaniak.resources.kdrive import Kdrive, AsyncKdrive
from infomaniak.resources.etickets import Etickets, AsyncEtickets
from infomaniak.resources.newsletter import Newsletter, AsyncNewsletter


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
        self.tasks = Tasks(self)
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
        self.tasks = AsyncTasks(self)
        self.url = AsyncUrl(self)
        self.video = AsyncVideo(self)
