# Cloud Kubernetes Data

The `cloud.kubernetes.data` resource exposes reference data used to provision Kubernetes services in Public Cloud.

## List Data

- No parameters.

```py
from typing import Any

from infomaniak import Client

client = Client()
data: dict[str, list[Any]] = client.cloud.kubernetes.data.list()
```

`dict[str, list[Any]]`:

- `packs`: List of Kubernetes Service packs.
- `versions`: List of Kubernetes versions.
- `regions`: List of Kubernetes regions.

## List Packs

- No parameters.

```py
from typing import Any

from infomaniak import Client

client = Client()
packs: list[dict[str, Any]] = client.cloud.kubernetes.data.packs()
```

`list[dict[str, Any]]`:

- `kaas_pack_id`: Kubernetes Service Pack unique identifier.
- `name`: Kubernetes Service Pack name.
- `description`: Kubernetes Service Pack description.
- `price_per_hour`: Current Kubernetes Service Pack price per hour of usage.
- `limit_per_project`: Maximum number of Kubernetes Services for this pack per project (`null` means unlimited).
- `is_active`: Whether the pack is currently active.

## List Versions

- No parameters.

```py
from infomaniak import Client

client = Client()
versions: list[str] = client.cloud.kubernetes.data.versions()
```

`list[str]`:

- Kubernetes Service versions available for creation.

## List Regions

- No parameters.

```py
from infomaniak import Client

client = Client()
regions: list[str] = client.cloud.kubernetes.data.regions()
```

`list[str]`:

- Kubernetes Service regions available for creation.

## List Reagions (Compatibility Alias)

- No parameters.

```py
from infomaniak import Client

client = Client()
regions_alias: list[str] = client.cloud.kubernetes.data.reagions()
```

`list[str]`:

- Same output as `regions()`.

## List Availability Zones

- `region`: Public Cloud region to use for KaaS (for example `dc3-a`).

```py
from infomaniak import Client

client = Client()
zones: list[str] = client.cloud.kubernetes.data.zones(region="dc3-a")
```

`list[str]`:

- Availability zones for the provided region.

## List Flavors

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `region`: Optional Public Cloud region filter.
- `filter_`: Optional API flavor filters.
- `page`: Optional page number.
- `items`: Optional item count per page.

```py
from typing import Any

from infomaniak import Client
from infomaniak.utils import plist

client = Client()
flavors: plist[dict[str, Any]] = client.cloud.kubernetes.data.flavors(
    public_cloud_id=13247,
    public_cloud_project_id=30802,
    region="dc4-a",
    page=1,
    items=20,
)
```

`plist[dict[str, Any]]`:

- `name`: Flavor name.
- `cpu`: Number of vCPUs.
- `ram`: RAM amount.
- `storage`: Storage amount.
- `is_available`: Whether the flavor is currently available.
- `is_memory_optimized`: Whether the flavor is memory optimized.
- `is_iops_optimized`: Whether the flavor is IOPS optimized.
- `is_gpu_optimized`: Whether the flavor is GPU optimized.
- `rates`: Pricing rates.

## List Flavor (Compatibility Alias)

- Same parameters as `flavors()`.

```py
from typing import Any

from infomaniak import Client
from infomaniak.utils import plist

client = Client()
flavor: plist[dict[str, Any]] = client.cloud.kubernetes.data.flavor(
    public_cloud_id=13247,
    public_cloud_project_id=30802,
    region="dc4-a",
)
```

`plist[dict[str, Any]]`:

- Same output as `flavors()`.

## List Flavor Filters

- `public_cloud_id`: Unique identifier of the Public Cloud account.
- `public_cloud_project_id`: Unique identifier of the Public Cloud project.
- `region`: Public Cloud region to use for KaaS.

```py
from typing import Any

from infomaniak import Client

client = Client()
filters: dict[str, Any] = client.cloud.kubernetes.data.flavor_filters(
    public_cloud_id=99854,
    public_cloud_project_id=89164,
    region="dc3-a",
)
```

`dict[str, Any]`:

- `gpu_types`: Available GPU filter values.
