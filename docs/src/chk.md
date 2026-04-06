# CHK

The `chk` resource lets you create, list, and update short URLs, and inspect your shortener quota.

## Create

- `url`: URL to shorten.
- `expiration_date`: Optional Unix timestamp for short URL expiration.

```py
from infomaniak import Client
from infomaniak.models import ChkShortUrlResponse

client = Client()
response: ChkShortUrlResponse = client.chk.create(
    url="https://www.infomaniak.com",
    expiration_date=1633435186,
)
```

`ChkShortUrlResponse`:

- `result`: Request result (`success`, `error`, `asynchronous`).
- `data`: Created short URL object.

`data` (`ChkShortUrl`):

- `code`: Generated short URL code.
- `url`: Original URL.
- `created_at`: Creation Unix timestamp.
- `expiration_date`: Expiration Unix timestamp, when set.

## List

- `order_by`: Optional ordering field (`code`, `url`, `created_at`, `expiration_date`).
- `order_direction`: Optional ordering direction (`ASC`, `DESC`).
- `search`: Optional search value.
- `page`: Optional page number.
- `items`: Optional number of items returned per page.

```py
from infomaniak import Client
from infomaniak.models import ChkShortUrl
from infomaniak.utils import plist

client = Client()
short_urls: plist[ChkShortUrl] = client.chk.list(
    order_by="expiration_date",
    order_direction="DESC",
    search="example",
    page=1,
    items=93,
)
```

`plist[ChkShortUrl]`:

- `total`: Total number of records.
- `page`: Current page index.
- `pages`: Number of available pages.
- `[]`: List of `ChkShortUrl` records.

## Update

- `short_url_code`: Short URL code to update.
- `expiration_date`: Optional Unix timestamp for short URL expiration.

```py
from infomaniak import Client
from infomaniak.models import ChkShortUrlResponse

client = Client()
response: ChkShortUrlResponse = client.chk.update(
    short_url_code="czhS2Gn",
    expiration_date=1633435186,
)
```

`ChkShortUrlResponse`:

- `result`: Request result (`success`, `error`, `asynchronous`).
- `data`: Updated short URL object (`ChkShortUrl`).

## Quota

```py
from infomaniak import Client
from infomaniak.models import ChkQuota

client = Client()
quota: ChkQuota = client.chk.quota()
```

`ChkQuota`:

- `quota`: Current number of short URLs.
- `limit`: Maximum number of short URLs.
