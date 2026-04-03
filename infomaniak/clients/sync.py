
import httpx
from typing import Any
from infomaniak.constants import API
from .__root__ import RootClient


class AsyncBaseClient(RootClient):
    """Shared async transport for all SDK resources."""

    def __init__(
        self,
        token: str | None = None,
        base_url: str = API,
        timeout: float = 30.0,
        transport: httpx.AsyncBaseTransport | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(token, base_url, timeout, transport, headers)

        self._client: httpx.AsyncClient = httpx.AsyncClient(
            base_url=self._base_url,
            headers=self._headers,
            timeout=self._timeout,
            transport=transport,
        )

    async def request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> httpx.Response:
        return await self._client.request(method, path, **kwargs)

    async def _request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> httpx.Response:
        return await self.request(method, path, **kwargs)

    async def get(self, path: str, **kwargs: Any) -> httpx.Response:
        return await self.request("GET", path, **kwargs)

    async def post(self, path: str, **kwargs: Any) -> httpx.Response:
        return await self.request("POST", path, **kwargs)

    async def put(self, path: str, **kwargs: Any) -> httpx.Response:
        return await self.request("PUT", path, **kwargs)

    async def patch(self, path: str, **kwargs: Any) -> httpx.Response:
        return await self.request("PATCH", path, **kwargs)

    async def delete(self, path: str, **kwargs: Any) -> httpx.Response:
        return await self.request("DELETE", path, **kwargs)

    async def head(self, path: str, **kwargs: Any) -> httpx.Response:
        return await self.request("HEAD", path, **kwargs)

    async def options(self, path: str, **kwargs: Any) -> httpx.Response:
        return await self.request("OPTIONS", path, **kwargs)

    async def aclose(self) -> None:
        await self._client.aclose()

    async def __aenter__(self) -> "AsyncBaseClient":
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: Any,
    ) -> None:
        await self.aclose()
