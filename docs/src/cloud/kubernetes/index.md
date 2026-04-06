# Cloud Kubernetes

The `cloud.kubernetes` resource manages managed Kubernetes clusters in Public Cloud projects.

## Methods

- `cloud.kubernetes.list(...)`
- `cloud.kubernetes.create(...)`
- `cloud.kubernetes.get(...)`
- `cloud.kubernetes.delete(...)`
- `cloud.kubernetes.update(...)`
- `cloud.kubernetes.download(...)`
- `cloud.kubernetes.patch(...)`
- `cloud.kubernetes.kaas(...)`

## Nested Resources

- [Data](/cloud/kubernetes/data)
- [IP](/cloud/kubernetes/ip)
- [Pools](/cloud/kubernetes/pools)

::: warning
`cloud.kubernetes` endpoints are declared in the SDK but not implemented yet.
:::

## Usage

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")

# Not implemented yet:
# clusters = client.cloud.kubernetes.list(...)
```
