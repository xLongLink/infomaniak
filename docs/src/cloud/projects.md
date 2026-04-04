# Cloud Projects

The `cloud.projects` resource lets you create and inspect Public Cloud projects.

## Methods

- `cloud.projects.create(public_cloud_id, project_name, user_password, *, user_description=None, user_email=None)`
- `cloud.projects.list(public_cloud_id, *, with_=None)`
- `cloud.projects.get(public_cloud_id, public_cloud_project_id, *, with_=None)`

## Request models

### Create project request

- `project_name` (`str`, required)
- `user_password` (`str`, required)
- `user_description` (`str | None`, optional)
- `user_email` (`str | None`, optional)

## Returned models

- `CreatePublicCloudProjectResponse`
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

projects = client.cloud.projects.list(public_cloud_id=64258)
project = client.cloud.projects.get(
    public_cloud_id=64258,
    public_cloud_project_id=25454,
)
```
