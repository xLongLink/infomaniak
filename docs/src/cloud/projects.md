# Cloud Projects

The `cloud.projects` resource manages Public Cloud projects.

## Create Project

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `project_name`: Name for the new project.
- `user_password`: Password for the default project user.
- `user_description`: Optional description for the default project user.
- `user_email`: Optional email for the default project user.

```py
from infomaniak import Client
from infomaniak.models.cloud import CreatePublicCloudProjectResponse

client = Client()
created: CreatePublicCloudProjectResponse = client.cloud.projects.create(
    public_cloud_id=...,
    project_name=...,
    user_password=...,
)
```

`CreatePublicCloudProjectResponse`:

- `data`: Created project action payload.
- `result`: API operation status.

## Create Project with Invitation

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `project_name`: Name for the new project.
- `user_email`: Email address that receives the invitation.
- `user_description`: Optional description for the invited user.

```py
from infomaniak import Client
from infomaniak.models.cloud import PublicCloudProjectInvitationResponse

client = Client()
invited: PublicCloudProjectInvitationResponse = client.cloud.projects.create_with_invitation(
    public_cloud_id=...,
    project_name=...,
    user_email=...,
)
```

`PublicCloudProjectInvitationResponse`:

- `data`: Invitation payload.
- `result`: API operation status.

## Update Project

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the project to update.
- `name`: New project name (maximum `250` characters).

```py
from infomaniak import Client
from infomaniak.models.cloud import PublicCloudProjectAsyncActionResponse

client = Client()
updated: PublicCloudProjectAsyncActionResponse = client.cloud.projects.update(
    public_cloud_id=...,
    public_cloud_project_id=...,
    name=...,
)
```

`PublicCloudProjectAsyncActionResponse`:

- `data`: Asynchronous action payload.
- `result`: API operation status.

## Delete Project

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the project to delete.

```py
from infomaniak import Client
from infomaniak.models.cloud import PublicCloudProjectAsyncActionResponse

client = Client()
removed: PublicCloudProjectAsyncActionResponse = client.cloud.projects.delete(
    public_cloud_id=...,
    public_cloud_project_id=...,
)
```

`PublicCloudProjectAsyncActionResponse`:

- `data`: Asynchronous action payload.
- `result`: API operation status.

## List Projects

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `with_`: Optional response expansions.

```py
from infomaniak import Client
from infomaniak.models.cloud import PublicCloudProjectListResponse

client = Client()
projects: PublicCloudProjectListResponse = client.cloud.projects.list(public_cloud_id=...)
```

`PublicCloudProjectListResponse`:

- `data`: List of projects.
- `result`: API operation status.

## Get Project

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the project to retrieve.
- `with_`: Optional response expansions.

```py
from infomaniak import Client
from infomaniak.models.cloud import PublicCloudProject

client = Client()
project: PublicCloudProject = client.cloud.projects.get(
    public_cloud_id=...,
    public_cloud_project_id=...,
)
```

`PublicCloudProject`:

- `id`: Project identifier.
- `name`: Project name.
- `status`: Project status.
- `region`: Project region.
