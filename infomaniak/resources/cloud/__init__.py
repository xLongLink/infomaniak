from .config import Config, AsyncConfig
from .database import Database, AsyncDatabase
from .projects import Projects, AsyncProjects
from .kubernetes import Kubernetes, AsyncKubernetes
from infomaniak.resource import Resouce, AsyncResource


class Cloud(Resouce):
    """Cloud resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.config = Config(client)
        self.database = Database(client)
        self.kubernetes = Kubernetes(client)
        self.projects = Projects(client)


class AsyncCloud(AsyncResource):
    """Async cloud resources."""

    def __init__(self, client) -> None:
        super().__init__(client)
        self.config = AsyncConfig(client)
        self.database = AsyncDatabase(client)
        self.kubernetes = AsyncKubernetes(client)
        self.projects = AsyncProjects(client)


__all__ = [
    "Config",
    "AsyncConfig",
    "Database",
    "Kubernetes",
    "AsyncDatabase",
    "AsyncKubernetes",
    "Projects",
    "AsyncProjects",
    "Cloud",
    "AsyncCloud",
]
