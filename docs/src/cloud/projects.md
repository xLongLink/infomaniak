# Cloud Projects

The `cloud.projects` resource manages Public Cloud projects for a specific Public Cloud account.

## Create Project

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `project_name`: Name to assign to the new project.
- `user_password`: Password for the default project user.
- `user_description`: Optional description for the default project user.
- `user_email`: Optional email for the default project user.

**returns:** `CreatePublicCloudProjectResponse` with the asynchronous creation action metadata.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
created = client.cloud.projects.create(
    public_cloud_id=64258,
    project_name="MyProject",
    user_password="example",
)
```

## Create Project with Invitation

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `project_name`: Name to assign to the new project.
- `user_email`: Email address that will receive the project invitation.
- `user_description`: Optional description for the invited user.

**returns:** `PublicCloudProjectInvitationResponse` with invitation details and state.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
invited = client.cloud.projects.create_with_invitation(
    public_cloud_id=64258,
    project_name="MyProject",
    user_email="user@example.com",
)
```

## Update Project

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the project to update.
- `name`: New project name (maximum `250` characters).

**returns:** `PublicCloudProjectAsyncActionResponse` with the asynchronous update action metadata.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
updated = client.cloud.projects.update(
    public_cloud_id=64258,
    public_cloud_project_id=25454,
    name="RenamedProject",
)
```

## Delete Project

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the project to delete.

**returns:** `PublicCloudProjectAsyncActionResponse` with the asynchronous deletion action metadata.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
removed = client.cloud.projects.delete(
    public_cloud_id=64258,
    public_cloud_project_id=25454,
)
```

## List Projects

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `with_`: Optional extra response expansions requested from the API.

**returns:** `PublicCloudProjectListResponse` containing all matching projects.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
projects = client.cloud.projects.list(public_cloud_id=64258)
```

## Get Project

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the project to retrieve.
- `with_`: Optional extra response expansions requested from the API.

**returns:** `PublicCloudProject` with full details for the requested project.

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")
project = client.cloud.projects.get(
    public_cloud_id=64258,
    public_cloud_project_id=25454,
)
```
