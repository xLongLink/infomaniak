# Core Timezones

The `core.timezones` resource lets you list all available API timezones and display a specific timezone by ID.

## List Timezones

- `search`: Optional search string used to filter timezone names.
- `page`: Optional page number for paginated responses.
- `items`: Optional number of items returned per page.

```py
from infomaniak import Client
from infomaniak.models import Timezone
from infomaniak.utils import plist

client = Client()
timezones: plist[Timezone] = client.core.timezones.list(search="Europe", page=1, items=15)
```

`plist[Timezone]`:

- `[]`: A list containing `Timezone` objects.
- `page`: Current page number.
- `pages`: Total number of pages.
- `total`: Total number of records.

`Timezone`:

- `id`: Unique identifier of the timezone.
- `name`: Timezone name (for example `Europe/Zurich`).
- `gmt`: GMT offset (for example `01:00`).

## Display Timezone

- `timezone_id`: Unique identifier (ID) of the timezone.

```py
from infomaniak import Client
from infomaniak.models import Timezone

client = Client()
timezone: Timezone = client.core.timezones.display(timezone_id=414)
```

`Timezone`:

- `id`: Unique identifier of the timezone.
- `name`: Timezone name (for example `Europe/Zurich`).
- `gmt`: GMT offset (for example `01:00`).
