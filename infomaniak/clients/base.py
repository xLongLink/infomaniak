
import httpx
from typing import Any
from infomaniak.constants import API
from .__root__ import RootClient


class BaseClient(RootClient):
    """Shared sync transport for all SDK resources."""

    def __init__(
        self,
        token: str | None = None,
        base_url: str = API,
        timeout: float = 30.0,
        transport: httpx.BaseTransport | None = None,
        headers: dict[str, str] | None = None,
    ) -> None:
        super().__init__(token, base_url, timeout, transport, headers)

        self._client: httpx.Client = httpx.Client(
            base_url=self._base_url,
            headers=self._headers,
            timeout=self._timeout,
            transport=transport,
        )

    def request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> httpx.Response:
        return self._client.request(method, path, **kwargs)

    def _request(
        self,
        method: str,
        path: str,
        **kwargs: Any,
    ) -> httpx.Response:
        return self.request(method, path, **kwargs)

    def get(self, path: str, **kwargs: Any) -> httpx.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> httpx.Response:
        return self.request("POST", path, **kwargs)

    def put(self, path: str, **kwargs: Any) -> httpx.Response:
        return self.request("PUT", path, **kwargs)

    def patch(self, path: str, **kwargs: Any) -> httpx.Response:
        return self.request("PATCH", path, **kwargs)

    def delete(self, path: str, **kwargs: Any) -> httpx.Response:
        return self.request("DELETE", path, **kwargs)

    def head(self, path: str, **kwargs: Any) -> httpx.Response:
        return self.request("HEAD", path, **kwargs)

    def options(self, path: str, **kwargs: Any) -> httpx.Response:
        return self.request("OPTIONS", path, **kwargs)

    def close(self) -> None:
        self._client.close()

    def __enter__(self) -> "BaseClient":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: Any,
    ) -> None:
        self.close()

