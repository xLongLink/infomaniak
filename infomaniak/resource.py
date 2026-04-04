from infomaniak.clients import BaseClient, AsyncBaseClient


class Resouce:
    def __init__(self, client: BaseClient):
        self._client = client


class AsyncResource:
    def __init__(self, client: AsyncBaseClient):
        self._client = client
