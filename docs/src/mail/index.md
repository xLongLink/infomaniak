# Mail Overview

The `mail` domain exposes mailbox lifecycle operations and nested mailbox resources.

## Resources

- [`mailbox_management`](./mailbox_management)
- [`mailboxes`](./mailboxes)

## Quick usage

```py
from infomaniak import Client

client = Client(token="<token>")
mail = client.mail

mailbox_management = mail.mailbox_management
mailboxes = mail.mailboxes
```
