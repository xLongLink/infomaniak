# Core Overview

This section contains the `core` resources for the Infomaniak Python SDK.

Use this overview as the entry point for `core` endpoints.

## SDK Function Coverage

| Resource methods                                                                                                                   | Api Reference | Implemented |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------- |
| [`core.actions.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/actions.py)                      |               | No          |
| [`core.countries.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/countries.py)                  |               | No          |
| [`core.countries.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/countries.py)               |               | No          |
| [`core.events.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/events.py)                        |               | No          |
| [`core.events.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/events.py)                     |               | No          |
| [`core.ksuite.show`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/__init__.py)               |               | No          |
| [`core.ksuite.current`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/__init__.py)            |               | No          |
| [`core.ksuite.mailbox.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py)         |               | No          |
| [`core.ksuite.mailbox.primary`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py)     |               | No          |
| [`core.ksuite.mailbox.password`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py)    |               | No          |
| [`core.ksuite.mailbox.unlink`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py)      |               | No          |
| [`core.ksuite.mailbox.attach`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py)      |               | No          |
| [`core.languages.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/languages.py)                  |               | No          |
| [`core.languages.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/languages.py)               |               | No          |
| [`core.products.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/products.py)                    |               | No          |
| [`core.profile.avatar.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/avatar.py)      |               | No          |
| [`core.profile.avatar.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/avatar.py)      |               | No          |
| [`core.profile.email.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/email.py)          |               | No          |
| [`core.profile.email.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/email.py)       |               | No          |
| [`core.profile.email.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/email.py)        |               | No          |
| [`core.profile.info.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/info.py)            |               | No          |
| [`core.profile.info.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/info.py)          |               | No          |
| [`core.profile.password.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/password.py)    |               | No          |
| [`core.profile.password.add`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/password.py)     |               | No          |
| [`core.profile.password.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/password.py) |               | No          |
| [`core.profile.phone.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/phone.py)          |               | No          |
| [`core.profile.phone.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/phone.py)       |               | No          |
| [`core.profile.phone.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/phone.py)        |               | No          |
| [`core.tasks.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/tasks.py)                          |               | No          |
| [`core.tasks.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/tasks.py)                       |               | No          |
| [`core.timezones.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/timezones.py)                  |               | No          |
| [`core.timezones.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/timezones.py)               |               | No          |
| [`core.user.invite`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/__init__.py)                 |               | Yes         |
| [`core.user.cancel`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/__init__.py)                 |               | Yes         |
| [`core.user.revoke`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/__init__.py)                 |               | Yes         |
| [`core.user.accounts.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py)          |               | No          |
| [`core.user.accounts.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py)       |               | No          |
| [`core.user.accounts.products`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py)      |               | No          |
| [`core.user.accounts.tags`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py)          |               | No          |
| [`core.user.accounts.services`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py)      |               | No          |
| [`core.user.accounts.apps`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py)          |               | No          |
| [`core.user.accounts.teams`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py)         |               | No          |
| [`core.user.accounts.users`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py)         |               | No          |
| [`core.user.teams.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py)                |               | No          |
| [`core.user.teams.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py)              |               | No          |
| [`core.user.teams.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py)                 |               | No          |
| [`core.user.teams.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py)              |               | No          |
| [`core.user.teams.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py)              |               | No          |
