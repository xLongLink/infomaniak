# Cloud Kubernetes

The `cloud.kubernetes` resource manages managed Kubernetes clusters in Public Cloud projects.

## List Kubernetes Clusters

- `public_cloud_id`: Unique identifier of the Public Cloud account (required when `public_cloud_project_id` is provided).
- `public_cloud_project_id`: Optional unique identifier of the Public Cloud project. If omitted, the account-wide endpoint is used.
- `account_id`: Unique identifier of the account (required when listing all Kubernetes services across Public Clouds).
- `with_`: Optional extra response expansions requested from the API.
- `filter_`: Optional API filters.
- `return_`: Optional return mode (for example `total`).
- `limit`: Optional offset-based pagination limit.
- `skip`: Optional offset-based pagination offset.
- `page`: Optional page-based pagination page number.
- `per_page`: Optional page-based pagination item count.
- `order_by`: Optional field used for sorting.
- `order`: Optional sorting direction (`asc` or `desc`).
- `order_for`: Optional per-field sorting order.

**returns:** `plist[dict[str, Any]]` containing matching Kubernetes clusters.

```py
from infomaniak import Client

client = Client()
clusters = client.cloud.kubernetes.list(
    public_cloud_id=...,
    public_cloud_project_id=...,
)

all_clusters = client.cloud.kubernetes.list(
    account_id=100001,
    order_by="name",
    order="asc",
)
```

## Create Kubernetes Cluster

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `payload`: Cluster creation payload sent to the API.

**returns:** `dict[str, Any]` containing the API creation response.

```py
from infomaniak import Client

client = Client()
created = client.cloud.kubernetes.create(
    public_cloud_id=...,
    public_cloud_project_id=...,
    payload=...,
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

client = Client()
cluster = client.cloud.kubernetes.get(
    public_cloud_id=...,
    public_cloud_project_id=...,
    kubernetes_id=...,
)
```

## Delete Kubernetes Cluster

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `kubernetes_id`: Unique identifier of the Kubernetes cluster.

**returns:** `dict[str, Any]` with operation status.

```py
from infomaniak import Client

client = Client()
removed = client.cloud.kubernetes.delete(
    public_cloud_id=...,
    public_cloud_project_id=...,
    kubernetes_id=...,
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

client = Client()
updated = client.cloud.kubernetes.update(
    public_cloud_id=...,
    public_cloud_project_id=...,
    kubernetes_id=...,
    payload=...,
)
```

## Download Kubernetes Kubeconfig

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `kubernetes_id`: Unique identifier of the Kubernetes cluster.

**returns:** `dict[str, Any]` containing kubeconfig download payload.

```py
from infomaniak import Client

client = Client()
kubeconfig = client.cloud.kubernetes.download(
    public_cloud_id=...,
    public_cloud_project_id=...,
    kubernetes_id=...,
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

client = Client()
patched = client.cloud.kubernetes.patch(
    public_cloud_id=...,
    public_cloud_project_id=...,
    kubernetes_id=...,
    payload=...,
)
```

## List KaaS Templates

- `account_id`: Optional account identifier to scope available templates.

**returns:** `plist[dict[str, Any]]` containing available templates.

```py
from infomaniak import Client

client = Client()
templates = client.cloud.kubernetes.kaas(account_id=...)
```

## Nested Resources

- [Data](/cloud/kubernetes/data)
- [IP](/cloud/kubernetes/ip)
- [Pools](/cloud/kubernetes/pools)
