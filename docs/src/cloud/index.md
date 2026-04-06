# Cloud

The `cloud` resource exposes top-level Public Cloud product endpoints and nested resources.

## Methods

- `cloud.list(account_id)`
- `cloud.get(public_cloud_id)`
- `cloud.update(public_cloud_id, bill_reference=None, customer_name=None, description=None)`

## List Public Clouds

- `account_id`: Unique identifier of the account.

**returns:** `PaginatedList[PublicCloud]` containing Public Cloud products and pagination metadata.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
clouds = client.cloud.list(account_id=12345)
```

## Get Public Cloud

- `public_cloud_id`: Unique identifier of the Public Cloud product.

**returns:** `PublicCloud` with full details for the requested product.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
cloud = client.cloud.get(public_cloud_id=64258)
```

## Update Public Cloud

- `public_cloud_id`: Unique identifier of the Public Cloud product.
- `bill_reference`: Optional billing reference (minimum length `2`).
- `customer_name`: Optional customer name (minimum length `2`).
- `description`: Optional description (minimum length `2`).

**returns:** `PublicCloudBoolResponse` with the API operation status.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
updated = client.cloud.update(
    public_cloud_id=64258,
    customer_name="Acme Team",
    description="Main production cloud",
)
```

# Cloud

The Cloud section groups SDK resources used to manage Public Cloud accounts, projects, managed databases, and Kubernetes clusters.

## Resources

- [Config](/cloud/config)
- [Projects](/cloud/projects)
- [Database](/cloud/database/)
- [Kubernetes](/cloud/kubernetes/)
