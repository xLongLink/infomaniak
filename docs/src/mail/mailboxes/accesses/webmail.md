# Mail Mailboxes Accesses Webmail

`client.mail.mailboxes.accesses.webmail` groups team and user webmail access endpoints.

## Nested Resources

- [`team`](./webmail/team)
- [`user`](./webmail/user)

## Quick usage

```py
from infomaniak import Client

client = Client(token="<token>")
webmail = client.mail.mailboxes.accesses.webmail

team_access = webmail.team
user_access = webmail.user
```
