# Overview

Welcome to the **Infomaniak SDK for Python** documentation.

Use the sidebar to navigate by API domain. Each section mirrors the SDK resource tree under `infomaniak/resources` so you can quickly map documentation pages to SDK entry points.

## Getting started

```py
from infomaniak import Client

client = Client(token="<your-api-token>")
core = client.core
```

## Available API domains

- AI
- Backup
- Cloud
- Core
- DNS
- kChat
- kDrive
- kMeet
- Mail
- Newsletter
- Radio
- Tickets
- URL
- Video
- VOD

::: tip
Looking for a specific endpoint? Open the related domain in the sidebar and start from its **Overview** page.
:::


## SDK function coverage

| Resource methods | Api Reference | Implemented |
|---|---|---|
| [`cloud.database.backups.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/backups.py) |  | ❌ |
| [`cloud.database.backups.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/backups.py) |  | ❌ |
| [`cloud.database.backups.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/backups.py) |  | ❌ |
| [`cloud.database.config.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py) |  | ❌ |
| [`cloud.database.config.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py) |  | ❌ |
| [`cloud.database.config.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py) |  | ❌ |
| [`cloud.database.config.remove`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py) |  | ❌ |
| [`cloud.database.config.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/config.py) |  | ❌ |
| [`cloud.database.data.packs`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/data.py) |  | ❌ |
| [`cloud.database.data.regions`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/data.py) |  | ❌ |
| [`cloud.database.data.types`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/data.py) |  | ❌ |
| [`cloud.database.ip.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/ip.py) |  | ❌ |
| [`cloud.database.ip.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/ip.py) |  | ❌ |
| [`cloud.database.ip.remove`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/ip.py) |  | ❌ |
| [`cloud.database.restore.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/restore.py) |  | ❌ |
| [`cloud.database.restore.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/restore.py) |  | ❌ |
| [`cloud.database.scheduled.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |  | ❌ |
| [`cloud.database.scheduled.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |  | ❌ |
| [`cloud.database.scheduled.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |  | ❌ |
| [`cloud.database.scheduled.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |  | ❌ |
| [`cloud.database.scheduled.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/database/scheduled.py) |  | ❌ |
| [`cloud.kubernetes.data.flavors`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py) |  | ❌ |
| [`cloud.kubernetes.data.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py) |  | ❌ |
| [`cloud.kubernetes.data.reagions`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py) |  | ✅ |
| [`cloud.kubernetes.data.regions`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py) |  | ❌ |
| [`cloud.kubernetes.data.versions`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py) |  | ❌ |
| [`cloud.kubernetes.data.zones`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/data.py) |  | ❌ |
| [`cloud.kubernetes.ip.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/ip.py) |  | ❌ |
| [`cloud.kubernetes.ip.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/ip.py) |  | ❌ |
| [`cloud.kubernetes.ip.remove`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/ip.py) |  | ❌ |
| [`cloud.kubernetes.ip.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/ip.py) |  | ❌ |
| [`cloud.kubernetes.pools.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py) |  | ❌ |
| [`cloud.kubernetes.pools.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py) |  | ❌ |
| [`cloud.kubernetes.pools.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py) |  | ❌ |
| [`cloud.kubernetes.pools.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py) |  | ❌ |
| [`cloud.kubernetes.pools.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/cloud/kubernetes/pools.py) |  | ❌ |
| [`core.actions.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/actions.py) |  | ❌ |
| [`core.countries.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/countries.py) |  | ❌ |
| [`core.countries.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/countries.py) |  | ❌ |
| [`core.events.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/events.py) |  | ❌ |
| [`core.events.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/events.py) |  | ❌ |
| [`core.ksuite.mailbox.attach`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py) |  | ❌ |
| [`core.ksuite.mailbox.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py) |  | ❌ |
| [`core.ksuite.mailbox.password`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py) |  | ❌ |
| [`core.ksuite.mailbox.primary`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py) |  | ❌ |
| [`core.ksuite.mailbox.unlink`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/ksuite/mailbox.py) |  | ❌ |
| [`core.languages.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/languages.py) |  | ❌ |
| [`core.languages.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/languages.py) |  | ❌ |
| [`core.products.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/products.py) |  | ❌ |
| [`core.profile.avatar.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/avatar.py) |  | ❌ |
| [`core.profile.avatar.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/avatar.py) |  | ❌ |
| [`core.profile.email.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/email.py) |  | ❌ |
| [`core.profile.email.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/email.py) |  | ❌ |
| [`core.profile.email.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/email.py) |  | ❌ |
| [`core.profile.info.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/info.py) |  | ❌ |
| [`core.profile.info.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/info.py) |  | ❌ |
| [`core.profile.password.add`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/password.py) |  | ❌ |
| [`core.profile.password.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/password.py) |  | ❌ |
| [`core.profile.password.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/password.py) |  | ❌ |
| [`core.profile.phone.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/phone.py) |  | ❌ |
| [`core.profile.phone.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/phone.py) |  | ❌ |
| [`core.profile.phone.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/profile/phone.py) |  | ❌ |
| [`core.tasks.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/tasks.py) |  | ❌ |
| [`core.tasks.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/tasks.py) |  | ❌ |
| [`core.timezones.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/timezones.py) |  | ❌ |
| [`core.timezones.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/timezones.py) |  | ❌ |
| [`core.user.accounts.apps`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.display`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.products`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.services`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.tags`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.teams`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.accounts.users`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/accounts.py) |  | ❌ |
| [`core.user.teams.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py) |  | ❌ |
| [`core.user.teams.delete`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py) |  | ❌ |
| [`core.user.teams.get`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py) |  | ❌ |
| [`core.user.teams.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py) |  | ❌ |
| [`core.user.teams.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/core/user/teams.py) |  | ❌ |
| [`domain.dnssec.check`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/dnssec.py) |  | ❌ |
| [`domain.dnssec.disable`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/dnssec.py) |  | ❌ |
| [`domain.dnssec.enable`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/dnssec.py) |  | ❌ |
| [`domain.nameservers.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/nameservers.py) |  | ❌ |
| [`domain.order.check`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/order.py) |  | ❌ |
| [`domain.order.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/order.py) |  | ❌ |
| [`domain.order.transfer`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/order.py) |  | ❌ |
| [`domain.zone.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/domain/zone.py) |  | ❌ |
| [`kchat.bots.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/bots.py) |  | ❌ |
| [`kchat.channels.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/channels.py) |  | ❌ |
| [`kchat.commands.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/commands.py) |  | ❌ |
| [`kchat.emoji.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/emoji.py) |  | ❌ |
| [`kchat.files.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/files.py) |  | ❌ |
| [`kchat.groups.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/groups.py) |  | ❌ |
| [`kchat.insights.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/insights.py) |  | ❌ |
| [`kchat.posts.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/posts.py) |  | ❌ |
| [`kchat.preferences.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/preferences.py) |  | ❌ |
| [`kchat.reactions.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/reactions.py) |  | ❌ |
| [`kchat.roles.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/roles.py) |  | ❌ |
| [`kchat.status.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/status.py) |  | ❌ |
| [`kchat.system.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/system.py) |  | ❌ |
| [`kchat.teams.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/teams.py) |  | ❌ |
| [`kchat.threads.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/threads.py) |  | ❌ |
| [`kchat.users.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/users.py) |  | ❌ |
| [`kchat.webhooks.non_implemented`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kchat/webhooks.py) |  | ❌ |
| [`kmeet.plan.plan_a_conference`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kmeet/plan.py) |  | ❌ |
| [`kmeet.room.get_room_settings`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/kmeet/room.py) |  | ❌ |
| [`url.short.create`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/url/short.py) |  | ❌ |
| [`url.short.list`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/url/short.py) |  | ❌ |
| [`url.short.quota`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/url/short.py) |  | ❌ |
| [`url.short.update`](https://github.com/XLongLink/infomaniak/blob/main/infomaniak/resources/url/short.py) |  | ❌ |
