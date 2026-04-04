# Cloud Config

The `cloud.config` resource lets you fetch Public Cloud configuration values for an account.

## Methods

- `cloud.config.get(account_id)`

## Request models

### Get config request

- `account_id` (`int`, required): unique identifier of the account.

## Returned models

- `PublicCloudConfigResponse`
- `PublicCloudConfig`

## Usage

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")

config = client.cloud.config.get(account_id=11133)
print(config.data.free_tier)
```
