# Cloud Config

The `cloud.config` resource lets you fetch Public Cloud account configuration values.

## Get Config

- `account_id`: Unique identifier of the account.


```py
from infomaniak import Client

client = Client()
config: PublicCloudConfig = client.cloud.config.get(account_id=...)
```

`PublicCloudConfig`:

- `free_tier`: Amount of free tier credit available for the account.
- `free_tier_used`: Amount of free tier credit already consumed.
- `account_resource_level`: Resource level assigned to the account.
- `valid_from`: Unix timestamp indicating when the configuration becomes valid.
- `valid_to`: Unix timestamp indicating when the configuration expires.
- `project_count`: Number of projects currently attached to the account.
