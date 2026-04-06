# Cloud Config

The `cloud.config` resource lets you fetch Public Cloud account configuration values.

## Get Config

- `account_id`: Unique identifier of the account.

**returns:** `PublicCloudConfigResponse` containing `PublicCloudConfig` data.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
config = client.cloud.config.get(account_id=11133)
print(config.data.free_tier)
```

## Returned Models

- `PublicCloudConfigResponse`
- `PublicCloudConfig`
