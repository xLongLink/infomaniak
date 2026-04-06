# Core Actions

The `core.actions` resource lets you list all available action types and fetch one action by its unique identifier.

## List Actions

- `search`: Optional search string used to filter action codes.

```py
from infomaniak import Client
from infomaniak.models import Action

client = Client()
actions: list[Action] = client.core.actions.list(search="example")
```

`list[Action]`:

- `id`: Unique identifier of the action.
- `code`: Action code.
- `description`: Action description.

## Get Action

- `action_id`: Unique identifier of the action to request.

```py
from infomaniak import Client
from infomaniak.models import Action

client = Client()
action: Action = client.core.actions.get(action_id=18134)
```

`Action`:

- `id`: Unique identifier of the action.
- `code`: Action code.
- `description`: Action description.
