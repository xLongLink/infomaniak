# Mail Mailboxes

`client.mail.mailboxes` is the navigation root for mailbox-scoped resources.

## Nested Resources

- [`accesses`](./mailboxes/accesses)
- [`aliases`](./mailboxes/aliases)
- [`auto_reply`](./mailboxes/auto_reply)
- [`filters`](./mailboxes/filters)
- [`folders`](./mailboxes/folders)
- [`forwarding`](./mailboxes/forwarding)
- [`signatures`](./mailboxes/signatures)
- [`users`](./mailboxes/users)

## Quick usage

```py
from infomaniak import Client

client = Client(token="<token>")
mailboxes = client.mail.mailboxes

aliases = mailboxes.aliases
filters = mailboxes.filters
```
