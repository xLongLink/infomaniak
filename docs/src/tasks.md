# Tasks

The `tasks` resource lets you list asynchronous jobs and inspect a single task by UUID.

## List Tasks

- `page`: Optional page number for paginated results.
- `per_page`: Optional number of items returned per page.

```py
from typing import Any
from infomaniak import Client

client = Client()
tasks: list[dict[str, Any]] = client.tasks.list(page=1, per_page=20)
```

`list[dict[str, Any]]`:

- `[]`: A list containing asynchronous task objects.

Each task object may include:

- `uuid`: Universally unique task identifier.
- `status`: Current task status (`spooled`, `running`, `executed`, `failed`).
- `created_at`: Creation timestamp.
- `updated_at`: Last update timestamp.
- `executed_at`: Execution timestamp.
- `finished_at`: Completion timestamp.
- `response`: Asynchronous response payload.
- `error`: Asynchronous error payload (when present).

## Get Task

- `task_uuid`: Unique identifier (UUID) of the asynchronous task.

```py
from typing import Any
from infomaniak import Client

client = Client()
task: dict[str, Any] = client.tasks.get(task_uuid="5cb09b3c-d03a-11eb-b8bc-0242ac130003")
```

`dict[str, Any]`:

- `uuid`: Universally unique task identifier.
- `status`: Current task status (`spooled`, `running`, `executed`, `failed`).
- `created_at`: Creation timestamp.
- `updated_at`: Last update timestamp.
- `executed_at`: Execution timestamp.
- `finished_at`: Completion timestamp.
- `response`: Asynchronous response payload.
- `error`: Asynchronous error payload (when present).
