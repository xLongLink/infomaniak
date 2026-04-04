# Cloud Projects

The `cloud.projects` resource lets you create, inspect, update, and delete Public Cloud projects.

## Methods

- `cloud.projects.create(public_cloud_id, project_name, user_password, *, user_description=None, user_email=None)`
- `cloud.projects.create_with_invitation(public_cloud_id, project_name, user_email, *, user_description=None)`
- `cloud.projects.update(public_cloud_id, public_cloud_project_id, name)`
- `cloud.projects.delete(public_cloud_id, public_cloud_project_id)`
- `cloud.projects.list(public_cloud_id, *, with_=None)`
- `cloud.projects.get(public_cloud_id, public_cloud_project_id, *, with_=None)`

## Request models

### Create project request

- `project_name` (`str`, required)
- `user_password` (`str`, required)
- `user_description` (`str | None`, optional)
- `user_email` (`str | None`, optional)

### Create project with invitation request

- `project_name` (`str`, required)
- `user_email` (`str`, required)
- `user_description` (`str | None`, optional)

### Update project request

- `name` (`str`, required, max length: `250`)

## Returned models

- `CreatePublicCloudProjectResponse`
- `PublicCloudProjectInvitationResponse`
- `PublicCloudProjectAsyncActionResponse`
- `PublicCloudProjectListResponse`
- `PublicCloudProject`

## Usage

```py
from infomaniak import Client

client = Client(token="YOUR_TOKEN")

creation = client.cloud.projects.create(
    public_cloud_id=64258,
    project_name="MyProject",
    user_password="example",
)

invitation = client.cloud.projects.create_with_invitation(
    public_cloud_id=64258,
    project_name="MyProject",
    user_email="user@example.com",
)

rename_task = client.cloud.projects.update(
    public_cloud_id=64258,
    public_cloud_project_id=25454,
    name="RenamedProject",
)

delete_task = client.cloud.projects.delete(
    public_cloud_id=64258,
    public_cloud_project_id=25454,
)

projects = client.cloud.projects.list(public_cloud_id=64258)
project = client.cloud.projects.get(
    public_cloud_id=64258,
    public_cloud_project_id=25454,
)
```
