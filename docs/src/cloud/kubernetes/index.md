# Cloud Kubernetes

The `cloud.kubernetes` resource manages managed Kubernetes clusters in Public Cloud projects.

## List Kubernetes Clusters

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `with_`: Optional extra response expansions requested from the API.

**returns:** `PaginatedList[dict[str, Any]]` containing matching Kubernetes clusters.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
clusters = client.cloud.kubernetes.list(
    public_cloud_id=64258,
    public_cloud_project_id=123456,
)
```

## Create Kubernetes Cluster

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `payload`: Cluster creation payload sent to the API.

**returns:** `dict[str, Any]` containing the API creation response.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
created = client.cloud.kubernetes.create(
    public_cloud_id=64258,
    public_cloud_project_id=123456,
    payload={
        "name": "prod-cluster",
        "region": "dc3",
        "version": "1.30",
    },
)
```

## Get Kubernetes Cluster

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `kubernetes_id`: Unique identifier of the Kubernetes cluster.
- `with_`: Optional extra response expansions requested from the API.

**returns:** `dict[str, Any]` containing Kubernetes cluster details.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
cluster = client.cloud.kubernetes.get(
    public_cloud_id=64258,
    public_cloud_project_id=123456,
    kubernetes_id=98765,
)
```

## Delete Kubernetes Cluster

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `kubernetes_id`: Unique identifier of the Kubernetes cluster.

**returns:** `dict[str, Any]` with operation status.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
removed = client.cloud.kubernetes.delete(
    public_cloud_id=64258,
    public_cloud_project_id=123456,
    kubernetes_id=98765,
)
```

## Update Kubernetes Cluster

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `kubernetes_id`: Unique identifier of the Kubernetes cluster.
- `payload`: Full cluster update payload sent to the API.

**returns:** `dict[str, Any]` with operation status.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
updated = client.cloud.kubernetes.update(
    public_cloud_id=64258,
    public_cloud_project_id=123456,
    kubernetes_id=98765,
    payload={"name": "renamed-cluster"},
)
```

## Download Kubernetes Kubeconfig

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `kubernetes_id`: Unique identifier of the Kubernetes cluster.

**returns:** `dict[str, Any]` containing kubeconfig download payload.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
kubeconfig = client.cloud.kubernetes.download(
    public_cloud_id=64258,
    public_cloud_project_id=123456,
    kubernetes_id=98765,
)
```

## Patch Kubernetes Cluster

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `kubernetes_id`: Unique identifier of the Kubernetes cluster.
- `payload`: Partial cluster update payload sent to the API.

**returns:** `dict[str, Any]` with operation status.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
patched = client.cloud.kubernetes.patch(
    public_cloud_id=64258,
    public_cloud_project_id=123456,
    kubernetes_id=98765,
    payload={"maintenance_window": {"day": "monday"}},
)
```

## List KaaS Templates

- `account_id`: Optional account identifier to scope available templates.

**returns:** `PaginatedList[dict[str, Any]]` containing available templates.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
templates = client.cloud.kubernetes.kaas(account_id=100001)
```

## Nested Resources

- [Data](/cloud/kubernetes/data)
- [IP](/cloud/kubernetes/ip)
- [Pools](/cloud/kubernetes/pools)
