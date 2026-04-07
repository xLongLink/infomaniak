import httpx
import pytest
from infomaniak import Client


def test_delete_kubernetes_cluster_returns_true() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "DELETE"
        assert request.url.path == "/1/public_clouds/1234/projects/5678/kaas/9012"
        return httpx.Response(200, json={"result": "success", "data": True})

    transport = httpx.MockTransport(handler)
    client = Client(token="test-token", transport=transport)

    deleted = client.cloud.kubernetes.delete(
        public_cloud_id=1234,
        public_cloud_project_id=5678,
        kaas_id=9012,
    )

    assert deleted is True


def test_delete_kubernetes_cluster_raises_when_data_is_false() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.method == "DELETE"
        return httpx.Response(200, json={"result": "success", "data": False})

    transport = httpx.MockTransport(handler)
    client = Client(token="test-token", transport=transport)

    with pytest.raises(ValueError, match="delete operation failed"):
        client.cloud.kubernetes.delete(
            public_cloud_id=1234,
            public_cloud_project_id=5678,
            kaas_id=9012,
        )
