# Cloud Kubernetes Pools

The `cloud.kubernetes.pools` resource manages Kubernetes instance pools (worker pools).

## List Instance Pools

- `public_cloud_id`: Unique identifier of the public cloud product.
- `public_cloud_project_id`: Unique identifier of the public cloud project.
- `kaas_id`: Unique identifier of the Kubernetes service.
- `filter_`: Optional API filters.
- `page`: Optional page number.
- `items`: Optional number of items per page.

```py
from typing import Any
from infomaniak import Client
from infomaniak.utils import plist

client = Client()
pools: plist[dict[str, Any]] = client.cloud.kubernetes.pools.list(
    public_cloud_id=8963,
    public_cloud_project_id=22892,
    kaas_id=75583,
    page=1,
    items=20,
)
```

`plist[dict[str, Any]]`:

- `instance_pool_id`: Unique identifier of the instance pool.
- `kaas_id`: Unique identifier of the Kubernetes service.
- `name`: Instance pool name.
- `open_stack_name`: OpenStack name of the instance pool.
- `availability_zone`: Availability zone used by the pool.
- `flavor`: Flavor used by pool instances.
- `minimum_instances`: Minimum number of instances.
- `maximum_instances`: Maximum number of instances, when set.
- `target_instances`: Target number of instances.
- `available_instances`: Number of currently available instances.
- `has_autoscaling`: Indicates whether autoscaling is enabled.
- `prefix`: Prefix used for instance names.
- `labels`: Kubernetes labels attached to pool instances.

## Create Instance Pool

- `public_cloud_id`: Unique identifier of the public cloud product.
- `public_cloud_project_id`: Unique identifier of the public cloud project.
- `kaas_id`: Unique identifier of the Kubernetes service.
- `flavor`: Flavor used by pool instances.
- `minimum_instances`: Minimum number of instances.
- `name`: Instance pool name.
- `availability_zone`: Optional availability zone.
- `labels`: Optional Kubernetes labels.
- `maximum_instances`: Optional maximum number of instances.
- `prefix`: Optional prefix for instance names.

```py
from infomaniak import Client

client = Client()
instance_pool_id: int = client.cloud.kubernetes.pools.create(
    public_cloud_id=2972,
    public_cloud_project_id=11151,
    kaas_id=49201,
    flavor="a1-ram2-disk20-perf1",
    minimum_instances=1,
    name="example",
)
```

`int`:

- Newly created instance pool identifier.

## Get Instance Pool

- `public_cloud_id`: Unique identifier of the public cloud product.
- `public_cloud_project_id`: Unique identifier of the public cloud project.
- `kaas_id`: Unique identifier of the Kubernetes service.
- `kaas_worker_pool_id`: Unique identifier of the instance pool.

```py
from typing import Any
from infomaniak import Client

client = Client()
pool: dict[str, Any] = client.cloud.kubernetes.pools.get(
    public_cloud_id=58932,
    public_cloud_project_id=30684,
    kaas_id=13175,
    kaas_worker_pool_id=71887,
)
```

`dict[str, Any]`:

- Instance pool object with the same fields as the List operation.

## Update Instance Pool

- `public_cloud_id`: Unique identifier of the public cloud product.
- `public_cloud_project_id`: Unique identifier of the public cloud project.
- `kaas_id`: Unique identifier of the Kubernetes service.
- `kaas_worker_pool_id`: Unique identifier of the instance pool.
- `labels`: Optional Kubernetes labels.
- `maximum_instances`: Optional maximum number of instances.
- `minimum_instances`: Optional minimum number of instances.
- `name`: Optional instance pool name.

```py
from infomaniak import Client

client = Client()
updated: bool = client.cloud.kubernetes.pools.update(
    public_cloud_id=18122,
    public_cloud_project_id=48358,
    kaas_id=88159,
    kaas_worker_pool_id=35696,
    maximum_instances=3,
    minimum_instances=1,
    name="example",
)
```

`bool`:

- `True` when the update request is accepted.
- `False` when the API reports no state change.

## Delete Instance Pool

- `public_cloud_id`: Unique identifier of the public cloud product.
- `public_cloud_project_id`: Unique identifier of the public cloud project.
- `kaas_id`: Unique identifier of the Kubernetes service.
- `kaas_worker_pool_id`: Unique identifier of the instance pool.

```py
from infomaniak import Client

client = Client()
deleted: bool = client.cloud.kubernetes.pools.delete(
    public_cloud_id=57966,
    public_cloud_project_id=87682,
    kaas_id=94268,
    kaas_worker_pool_id=81858,
)
```

`bool`:

- `True` when the delete request is accepted.
- `False` when the API reports no deletion.
