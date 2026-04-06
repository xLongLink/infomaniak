# Cloud Config

The `cloud.config` resource returns configuration values for a Public Cloud account.

## Get Config

- `account_id`: Unique identifier of the Public Cloud account.

```py
from infomaniak import Client
from infomaniak.models.cloud import PublicCloudConfig

client = Client()
config: PublicCloudConfig = client.cloud.config.get(account_id=...)
```

`PublicCloudConfig`:

- `free_tier`: Available free-tier credit.
- `free_tier_used`: Consumed free-tier credit.
- `account_resource_level`: Resource level assigned to the account.
- `valid_from`: Start UNIX timestamp for this config.
- `valid_to`: End UNIX timestamp for this config.
- `project_count`: Number of projects attached to the account.
