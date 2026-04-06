# Cloud Database

The `cloud.database` resource manages managed database services (DBaaS) in a Public Cloud project.

## Methods

- `cloud.database.list(public_cloud_id, public_cloud_project_id, with_=...)`
- `cloud.database.list_all(account_id, with_=...)`
- `cloud.database.create(public_cloud_id, public_cloud_project_id, name, pack_id, region, type_, version, backup_schedule=...)`
- `cloud.database.get(public_cloud_id, public_cloud_project_id, dbaas_id, with_=...)`
- `cloud.database.delete(public_cloud_id, public_cloud_project_id, dbaas_id, keep_backup_files=...)`
- `cloud.database.update(public_cloud_id, public_cloud_project_id, dbaas_id, name=..., pack_id=...)`
- `cloud.database.password(public_cloud_id, public_cloud_project_id, dbaas_id)`

## Nested Resources

- [Backups](/cloud/database/backups)
- [Config](/cloud/database/config)
- [Data](/cloud/database/data)
- [IP](/cloud/database/ip)
- [Restore](/cloud/database/restore)

## List Database Services

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `with_`: Optional expansion parameter (for example `projects` or `backups`).

**returns:** `plist[DatabaseService]` containing services and pagination metadata.

```py
from infomaniak import Client

client = Client()
services = client.cloud.database.list(
    public_cloud_id=...,
    public_cloud_project_id=...,
)
```

## Create Database Service

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `name`: Name of the database service.
- `pack_id`: Pack identifier for the selected service size.
- `region`: Public Cloud region where the service is deployed.
- `type_`: Database engine type.
- `version`: Database engine version.
- `backup_schedule`: Optional `CreateDatabaseServiceBackupScheduleRequest` object.

**returns:** `DatabaseServiceCreationResponse` with creation metadata.

```py
from infomaniak import Client

client = Client()
created = client.cloud.database.create(
    public_cloud_id=...,
    public_cloud_project_id=...,
    name=...,
    pack_id=...,
    region=...,
    type_=...,
    version=...,
)
```

## Get Database Service

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `dbaas_id`: Unique identifier of the managed database service.
- `with_`: Optional expansion parameter.

**returns:** `DatabaseService` with full service details.

## Update Database Service

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `dbaas_id`: Unique identifier of the managed database service.
- `name`: Optional new name.
- `pack_id`: Optional new pack identifier.

**returns:** `DatabaseServiceBoolResponse` with operation status.

## Delete Database Service

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `dbaas_id`: Unique identifier of the managed database service.
- `keep_backup_files`: Optional flag to preserve backup files.

**returns:** `DatabaseServiceBoolResponse` with operation status.

## Reset Root Password

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `dbaas_id`: Unique identifier of the managed database service.

**returns:** `DatabaseServiceConnectionResponse` containing updated connection data.

## Returned Models

- `DatabaseService`
- `DatabaseServiceCreationResponse`
- `DatabaseServiceConnectionResponse`
- `DatabaseServiceBoolResponse`
- `CreateDatabaseServiceBackupScheduleRequest`
