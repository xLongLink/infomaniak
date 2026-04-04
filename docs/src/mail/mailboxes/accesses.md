# Mail Mailboxes Accesses

Manage mailbox access-related endpoints under `client.mail.mailboxes.accesses`.

## Nested Resources

- [`devices`](./accesses/devices)
- [`invitations`](./accesses/invitations)
- [`webmail`](./accesses/webmail)

## Quick usage

```py
from infomaniak import Client

client = Client(token="<token>")
accesses = client.mail.mailboxes.accesses

devices = accesses.devices
invitations = accesses.invitations
```
