# Cloud Kubernetes IP

The `cloud.kubernetes.ip` resource manages API server IP filters for a Kubernetes cluster.

## List IP Filters

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `kaas_id`: Unique identifier of the Kubernetes service.

```py
from infomaniak import Client

client = Client()
ip_filters: list[str] = client.cloud.kubernetes.ip.list(
    public_cloud_id=...,
    public_cloud_project_id=...,
    kaas_id=...,
)
```

`list[str]`:

- List of configured IP filter CIDRs.

## Match IP Filters

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `kaas_id`: Unique identifier of the Kubernetes service.
- `ip_filters`: List of whitelist IP filters to apply.

```py
from infomaniak import Client

client = Client()
matched: bool = client.cloud.kubernetes.ip.match(
    public_cloud_id=...,
    public_cloud_project_id=...,
    kaas_id=...,
    ip_filters=["192.0.2.0/24"],
)
```

`bool`:

- Operation result returned by the API.

## Remove IP Filters

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `kaas_id`: Unique identifier of the Kubernetes service.

```py
from infomaniak import Client

client = Client()
removed: bool = client.cloud.kubernetes.ip.remove(
    public_cloud_id=...,
    public_cloud_project_id=...,
    kaas_id=...,
)
```

`bool`:

- Operation result returned by the API.
