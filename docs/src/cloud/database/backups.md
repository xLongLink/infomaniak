# Cloud Database Backups

The `cloud.database.backups` resource manages backup snapshots for a managed cloud database.

## Methods

- `cloud.database.backups.list(...)`
- `cloud.database.backups.get(...)`
- `cloud.database.backups.delete(...)`
- `cloud.database.backups.scheduled.*` (see [Scheduled Backups](/cloud/database/scheduled))

::: warning
`cloud.database.backups` endpoints are declared in the SDK but not implemented yet.
:::

## Usage

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")

# Not implemented yet:
# backups = client.cloud.database.backups.list(...)
```
