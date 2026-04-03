from infomaniak import Client, AsyncClient


class Resouce:
    def __init__(self, client: Client):
        self._client = client


class AsyncResource:
    def __init__(self, client: AsyncClient):
        self._client = client