# Cloud Overview

This section contains the `cloud` resources for the Infomaniak Python SDK.

## Methods

- `config.get(account_id)`

## Nested Resources

- `config`
- `database`
- `kubernetes`
- `projects`

## SDK Function Coverage

| Resource methods                                                                                                                        | Api Reference | Implemented |
| --------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------- |
| [`cloud.config.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/config.py)                           |               | Yes         |
| [`cloud.database.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/__init__.py)              |               | No          |
| [`cloud.database.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/__init__.py)            |               | No          |
| [`cloud.database.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/__init__.py)               |               | No          |
| [`cloud.database.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/__init__.py)            |               | No          |
| [`cloud.database.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/__init__.py)            |               | No          |
| [`cloud.database.password`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/__init__.py)          |               | No          |
| [`cloud.database.backups.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/backups.py)       |               | No          |
| [`cloud.database.backups.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/backups.py)        |               | No          |
| [`cloud.database.backups.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/backups.py)     |               | No          |
| [`cloud.database.config.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py)          |               | No          |
| [`cloud.database.config.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py)         |               | No          |
| [`cloud.database.config.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py)       |               | No          |
| [`cloud.database.config.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py)       |               | No          |
| [`cloud.database.config.remove`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py)       |               | No          |
| [`cloud.database.data.regions`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/data.py)          |               | No          |
| [`cloud.database.data.packs`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/data.py)            |               | No          |
| [`cloud.database.data.types`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/data.py)            |               | No          |
| [`cloud.database.ip.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/ip.py)                 |               | No          |
| [`cloud.database.ip.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/ip.py)               |               | No          |
| [`cloud.database.ip.remove`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/ip.py)               |               | No          |
| [`cloud.database.restore.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/restore.py)        |               | No          |
| [`cloud.database.restore.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/restore.py)     |               | No          |
| [`cloud.database.scheduled.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py)   |               | No          |
| [`cloud.database.scheduled.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |               | No          |
| [`cloud.database.scheduled.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py)    |               | No          |
| [`cloud.database.scheduled.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |               | No          |
| [`cloud.database.scheduled.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |               | No          |
| [`cloud.kubernetes.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/__init__.py)          |               | No          |
| [`cloud.kubernetes.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/__init__.py)        |               | No          |
| [`cloud.kubernetes.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/__init__.py)           |               | No          |
| [`cloud.kubernetes.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/__init__.py)        |               | No          |
| [`cloud.kubernetes.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/__init__.py)        |               | No          |
| [`cloud.kubernetes.download`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/__init__.py)      |               | No          |
| [`cloud.kubernetes.patch`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/__init__.py)         |               | No          |
| [`cloud.kubernetes.kaas`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/__init__.py)          |               | No          |
| [`cloud.kubernetes.data.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py)         |               | No          |
| [`cloud.kubernetes.data.versions`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py)     |               | No          |
| [`cloud.kubernetes.data.regions`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py)      |               | No          |
| [`cloud.kubernetes.data.reagions`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py)     |               | Yes         |
| [`cloud.kubernetes.data.zones`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py)        |               | No          |
| [`cloud.kubernetes.data.flavors`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py)      |               | No          |
| [`cloud.kubernetes.ip.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/ip.py)             |               | No          |
| [`cloud.kubernetes.ip.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/ip.py)           |               | No          |
| [`cloud.kubernetes.ip.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/ip.py)           |               | No          |
| [`cloud.kubernetes.ip.remove`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/ip.py)           |               | No          |
| [`cloud.kubernetes.pools.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py)       |               | No          |
| [`cloud.kubernetes.pools.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py)     |               | No          |
| [`cloud.kubernetes.pools.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py)        |               | No          |
| [`cloud.kubernetes.pools.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py)     |               | No          |
| [`cloud.kubernetes.pools.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py)     |               | No          |
| [`cloud.projects.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/projects.py)                         |               | Yes         |
| [`cloud.projects.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/projects.py)                           |               | Yes         |
| [`cloud.projects.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/projects.py)                            |               | Yes         |
