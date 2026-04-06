# Core Countries

The `core.countries` resource lets you list all available API countries and display a specific country by ID.

## List Countries

- `only_enabled`: Optional flag to return only enabled countries.
- `only_enabled_exception`: Optional country IDs to include when `only_enabled` is set.
- `search`: Optional search string used to filter country names.

```py
from infomaniak import Client
from infomaniak.models import Country

client = Client()
countries: list[Country] = client.core.countries.list(
    only_enabled=True,
    only_enabled_exception=[203],
    search="switz",
)
```

`list[Country]`:

- `[]`: A list containing `Country` objects.

`Country`:

- `id`: Unique identifier of the country.
- `name`: Name of the country.
- `short_name`: Short country code.
- `is_enabled`: Whether the country is enabled.

## Display Country

- `country_id`: Unique identifier (ID) of the country.

```py
from infomaniak import Client
from infomaniak.models import Country

client = Client()
country: Country = client.core.countries.display(country_id=203)
```

`Country`:

- `id`: Unique identifier of the country.
- `name`: Name of the country.
- `short_name`: Short country code.
- `is_enabled`: Whether the country is enabled.
