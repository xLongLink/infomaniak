from infomaniak.clients import AsyncBaseClient, BaseClient

# Load and connect resources to the clients
from infomaniak.resources.core import AsyncCore, Core
from infomaniak.resources.kmeet import AsyncKmeet, Kmeet


class Client(BaseClient):
    """Sync resource-based SDK client."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.core = Core(self)
        self.kmeet = Kmeet(self)


class AsyncClient(AsyncBaseClient):
    """Async resource-based SDK client."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.core = AsyncCore(self)
        self.kmeet = AsyncKmeet(self)
