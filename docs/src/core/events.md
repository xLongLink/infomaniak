# Core Events

The `core.events` resource lets you list platform events, display a specific event, and retrieve Public Cloud status information.

## List Events

- `date_from`: Optional Unix timestamp used to filter events starting from this date.
- `date_to`: Optional Unix timestamp used to filter events until this date.
- `event_type`: Optional event type filter (`internal`, `public`, `server`, `streaming`).
- `is_cyberattack`: Optional flag to filter cyberattack-related events.
- `locale`: Optional locale used for localized response fields (`de`, `en`, `es`, `fr`, `it`).
- `show_auto`: Optional flag to include automatically generated events.
- `status`: Optional event status filter (`inprogress`, `planned`, `reviewed`, `terminated`).
- `user_id`: Optional user identifier used to filter user-related events.
- `with_trashed`: Optional flag to include trashed events.
- `event_types`: Optional list of event types to filter multiple categories.

```py
from typing import Any
from infomaniak import Client

client = Client()
events: list[dict[str, Any]] = client.core.events.list(
    date_from=1704067200,
    date_to=1706745600,
    event_type="public",
    locale="en",
    status="planned",
)
```

`list[dict[str, Any]]`:

- `[]`: A list containing event objects returned by the API.

Each event object may include:

- `id`: Unique identifier of the event.
- `title`: Event title.
- `description`: Event description.
- `status`: Event status.
- `type`: Event type.
- `start_at`: Event start timestamp.
- `end_at`: Event end timestamp.

## Display Event

- `event_id`: Unique identifier (ID) of the event.

```py
from typing import Any
from infomaniak import Client

client = Client()
event: dict[str, Any] = client.core.events.display(event_id=12345)
```

`dict[str, Any]`:

- `id`: Unique identifier of the event.
- `title`: Event title.
- `description`: Event description.
- `status`: Event status.
- `type`: Event type.
- `start_at`: Event start timestamp.
- `end_at`: Event end timestamp.

## Public Cloud Status

No parameters.

```py
from typing import Any
from infomaniak import Client

client = Client()
public_cloud_status: dict[str, Any] = client.core.events.status()
```

`dict[str, Any]`:

- `status`: Global Public Cloud status.
- `components`: List of Public Cloud components and their statuses.
- `incidents`: List of current incidents, when present.
