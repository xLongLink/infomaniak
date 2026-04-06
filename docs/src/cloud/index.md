# Cloud

Allows to manage Public Cloud resources

## List Public Clouds

- `account_id`: Unique identifier of the account.

```py
from infomaniak import Client

client = Client()
plist: PaginatedList[PublicCloud] = client.cloud.list(account_id=...)
```

`PaginatedList[PublicCloud]`:

- `page`: Current page number returned by the API.
- `pages`: Total number of available pages.
- `items`: Total number of items across all pages.
- Each item in the list is a `PublicCloud` object.

`PublicCloud`:

- `id`: Unique identifier of the Public Cloud product.
- `account_id`: Unique identifier of the account that owns the product.
- `service_id`: Unique identifier of the linked service.
- `service_name`: Service name attached to the product.
- `customer_name`: Customer-facing name of the product.
- `internal_name`: Internal name of the product, when available.
- `created_at`: Unix timestamp indicating when the product was created.
- `expired_at`: Unix timestamp indicating when the product expires, when available.
- `version`: Version number of the product payload.
- `has_maintenance`: Whether the product currently has maintenance enabled.
- `is_locked`: Whether the product is locked.
- `has_operation_in_progress`: Whether an operation is currently in progress.
- `tags`: List of `PublicCloudTag` objects attached to the product.
- `unique_id`: Unique identifier of the product in the API payload.
- `is_free`: Whether the product is free of charge.
- `is_zero_price`: Whether the product currently has a zero price.
- `is_trial`: Whether the product is a trial product.
- `rights`: `PublicCloudRights` object describing granted permissions.
- `public_cloud_id`: Public Cloud identifier exposed by the API.
- `public_cloud`: `PublicCloudData` object containing billing and usage details.
- `deleted_at`: Unix timestamp indicating when the product was deleted, when available.
- `description`: Product description, when available.
- `bill_reference`: Billing reference, when available.
- `parent_id`: Identifier of the parent product, when available.
- `parent_service_id`: Identifier of the parent service, when available.
- `parent_service_name`: Name of the parent service, when available.
- `status`: `PublicCloudStatus` object with product status details, when available.
- `users`: Raw list of user objects returned by the API, when available.
- `admin`: Raw administrator object returned by the API, when available.
- `fqdn`: Fully qualified domain name of the product, when available.

## Get Public Cloud

- `public_cloud_id`: Unique identifier of the Public Cloud product.

```py
from infomaniak import Client

client = Client()
cloud: PublicCloud = client.cloud.get(public_cloud_id=...)
```

## Update Public Cloud

- `public_cloud_id`: Unique identifier of the Public Cloud product.
- `bill_reference`: Optional billing reference (minimum length `2`).
- `customer_name`: Optional customer name (minimum length `2`).
- `description`: Optional description (minimum length `2`).

```py
from infomaniak import Client

client = Client()
updated: PublicCloudBoolResponse = client.cloud.update(
    public_cloud_id=...,
    customer_name=...,
    description=...,
)
```

`PublicCloudBoolResponse`:

- `result`: API operation state.
- `data`: Boolean result payload or API status message.

# Cloud

The Cloud section groups SDK resources used to manage Public Cloud accounts, projects, managed databases, and Kubernetes clusters.

## Resources

- [Config](/cloud/config)
- [Projects](/cloud/projects)
- [Database](/cloud/database/)
- [Kubernetes](/cloud/kubernetes/)
