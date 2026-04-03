# kMeet

kMeet resources group conference-planning and room-related endpoints under `client.kmeet`.

## Available resources

- `plan`
- `room`

## Usage

```py
from infomaniak import Client

client = Client(token="<token>")

client.kmeet.plan.plan_a_conference()
client.kmeet.room.get_room_settings()
```

::: warning
These methods are placeholders and currently raise `NotImplementedError`.
:::
