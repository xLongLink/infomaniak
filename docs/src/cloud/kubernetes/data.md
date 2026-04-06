# Cloud Kubernetes Data

The `cloud.kubernetes.data` resource provides reference data for Kubernetes cluster provisioning.

## Methods

- `cloud.kubernetes.data.list(...)`
- `cloud.kubernetes.data.versions(...)`
- `cloud.kubernetes.data.regions(...)`
- `cloud.kubernetes.data.reagions(...)` (compatibility alias for `regions`)
- `cloud.kubernetes.data.zones(...)`
- `cloud.kubernetes.data.flavors(...)`

::: warning
`cloud.kubernetes.data` endpoints are declared in the SDK but not implemented yet.
:::

## Usage

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")

# Not implemented yet:
# versions = client.cloud.kubernetes.data.versions(...)
```
