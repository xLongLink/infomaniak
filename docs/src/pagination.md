# Pagination

Some SDK endpoints return paginated responses. These methods return a `plist[T]`, which is a list subclass that also includes pagination metadata.

## Paginated return type

`plist[T]` behaves like a normal list and exposes:

- `page`: Current page number.
- `pages`: Total number of available pages.
- `total`: Total number of items available across all pages.

## Single page example

```py
from infomaniak import Client
from infomaniak.models import Timezone
from infomaniak.utils import plist

client = Client()
timezones: plist[Timezone] = client.core.timezones.list(
    page=1,
    items=20,
)

print(timezones.page)
print(timezones.pages)
print(timezones.total)

for timezone in timezones:
    print(timezone.name)
```

## Iterate over all pages with `pages`

- `fetch_page`: A callable that accepts `page` and `items` keyword parameters.
- `page`: The first page number to fetch.
- `items`: Number of records to fetch on each page.

```py
from infomaniak import Client, pages
from infomaniak.models import Timezone
from infomaniak.utils import plist

client = Client()

fn = lambda *, page, items: client.core.timezones.list(
    search="Europe",
    page=page,
    items=items,
)

for timezone_page in pages(fn, page=1, items=100):
    typed_page: plist[Timezone] = timezone_page
    for timezone in typed_page:
        print(timezone.name)
```

`pages` returns an iterator of `plist[Timezone]` values:

- `page`: Current page index.
- `pages`: Total number of pages.
- `total`: Total number of matching timezones.
