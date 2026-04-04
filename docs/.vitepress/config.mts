import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Infomaniak SDK for Python',
  description: 'Python SDK documentation for the Infomaniak API.',
  srcDir: 'src',
  base: process.env.NODE_ENV === 'production' ? '/infomaniak/' : '/',
  cleanUrls: true,
  themeConfig: {
    socialLinks: [{ icon: 'github', link: 'https://github.com/XLongLink/infomaniak' }],
    sidebar: [
      {
        text: 'AI',
        link: '/ai/',
        collapsed: true,
      },
      {
        text: 'Backup',
        link: '/backup/',
        collapsed: true,
        items: [
          { text: 'Administrator', link: '/backup/administrator' },
          { text: 'Billing', link: '/backup/billing' },
          { text: 'Passwords', link: '/backup/passwords' },
          { text: 'Product', link: '/backup/product' },
          { text: 'Slots', link: '/backup/slots' },
        ],
      },
      {
        text: 'Cloud',
        link: '/cloud/',
        collapsed: true,
        items: [
          {
            text: 'Database',
            collapsed: true,
            items: [
              { text: 'Backups', link: '/cloud/database/backups' },
              { text: 'Config', link: '/cloud/database/config' },
              { text: 'Data', link: '/cloud/database/data' },
              { text: 'IP', link: '/cloud/database/ip' },
              { text: 'Restore', link: '/cloud/database/restore' },
              { text: 'Scheduled', link: '/cloud/database/scheduled' },
            ],
          },
          {
            text: 'Kubernetes',
            collapsed: true,
            items: [
              { text: 'Data', link: '/cloud/kubernetes/data' },
              { text: 'IP', link: '/cloud/kubernetes/ip' },
              { text: 'Pools', link: '/cloud/kubernetes/pools' },
            ],
          },
        ],
      },
      {
        text: 'Core',
        link: '/core/',
        collapsed: true,
        items: [
          { text: 'Actions', link: '/core/actions' },
          { text: 'Countries', link: '/core/countries' },
          { text: 'Events', link: '/core/events' },
          { text: 'Languages', link: '/core/languages' },
          { text: 'Products', link: '/core/products' },
          { text: 'Tasks', link: '/core/tasks' },
          { text: 'Timezones', link: '/core/timezones' },
          {
            text: 'kSuite',
            collapsed: true,
            items: [
              { text: 'Mailbox', link: '/core/ksuite/mailbox' },
            ],
          },
          {
            text: 'Profile',
            collapsed: true,
            items: [
              { text: 'Avatar', link: '/core/profile/avatar' },
              { text: 'Email', link: '/core/profile/email' },
              { text: 'Info', link: '/core/profile/info' },
              { text: 'Password', link: '/core/profile/password' },
              { text: 'Phone', link: '/core/profile/phone' },
            ],
          },
          {
            text: 'User',
            collapsed: true,
            items: [
              { text: 'Accounts', link: '/core/user/accounts' },
              { text: 'Teams', link: '/core/user/teams' },
            ],
          },
        ],
      },
      {
        text: 'DNS',
        link: '/dns/',
        collapsed: true,
        items: [
          { text: 'Domain', link: '/dns/domain' },
          { text: 'TLD', link: '/dns/tld' },
          { text: 'Zone', link: '/dns/zone' },
          {
            text: 'Domain',
            collapsed: true,
            items: [
              { text: 'DNSSEC', link: '/dns/domain/dnssec' },
              { text: 'Nameservers', link: '/dns/domain/nameservers' },
              { text: 'Order', link: '/dns/domain/order' },
            ],
          },
          {
            text: 'Zone',
            collapsed: true,
            items: [{ text: 'Records', link: '/dns/zone/records' }],
          },
        ],
      },
      {
        text: 'Domain',
        link: '/domain/',
        collapsed: true,
        items: [
          { text: 'DNSSEC', link: '/domain/dnssec' },
          { text: 'Nameservers', link: '/domain/nameservers' },
          { text: 'Order', link: '/domain/order' },
          { text: 'Zone', link: '/domain/zone' },
        ],
      },
      {
        text: 'kChat',
        link: '/kchat/',
        collapsed: true,
        items: [
          { text: 'Bots', link: '/kchat/bots' },
          { text: 'Channels', link: '/kchat/channels' },
          { text: 'Commands', link: '/kchat/commands' },
          { text: 'Emoji', link: '/kchat/emoji' },
          { text: 'Files', link: '/kchat/files' },
          { text: 'Groups', link: '/kchat/groups' },
          { text: 'Insights', link: '/kchat/insights' },
          { text: 'Posts', link: '/kchat/posts' },
          { text: 'Preferences', link: '/kchat/preferences' },
          { text: 'Reactions', link: '/kchat/reactions' },
          { text: 'Roles', link: '/kchat/roles' },
          { text: 'Status', link: '/kchat/status' },
          { text: 'System', link: '/kchat/system' },
          { text: 'Teams', link: '/kchat/teams' },
          { text: 'Threads', link: '/kchat/threads' },
          { text: 'Users', link: '/kchat/users' },
          { text: 'Webhooks', link: '/kchat/webhooks' },
        ],
      },
      {
        text: 'eTickets',
        link: '/etickets/',
        collapsed: true,
        items: [
          { text: 'Address', link: '/etickets/address' },
          { text: 'Customers', link: '/etickets/customers' },
          { text: 'Date', link: '/etickets/date' },
          { text: 'Reservations', link: '/etickets/reservations' },
          {
            text: 'Surveys',
            collapsed: true,
            items: [
              {
                text: 'Answers',
                collapsed: true,
                items: [
                  { text: 'Passes', link: '/etickets/surveys/answers/passes' },
                  { text: 'Tickets', link: '/etickets/surveys/answers/tickets' },
                ],
              },
            ],
          },
          { text: 'Ticket', link: '/etickets/ticket' },
        ],
      },
      {
        text: 'kDrive',
        link: '/kdrive/',
        collapsed: true,
      },
      {
        text: 'kMeet',
        link: '/kmeet/',
        collapsed: true,
        items: [
          { text: 'Plan', link: '/kmeet/plan' },
          { text: 'Room', link: '/kmeet/room' },
        ],
      },
      {
        text: 'Mail',
        link: '/mail/',
        collapsed: true,
        items: [
          { text: 'Mailbox Management', link: '/mail/mailbox_management' },
          {
            text: 'Mailboxes',
            collapsed: true,
            items: [
              { text: 'Accesses', link: '/mail/mailboxes/accesses' },
              { text: 'Aliases', link: '/mail/mailboxes/aliases' },
              { text: 'Auto Reply', link: '/mail/mailboxes/auto_reply' },
              { text: 'Filters', link: '/mail/mailboxes/filters' },
              { text: 'Folders', link: '/mail/mailboxes/folders' },
              { text: 'Forwarding', link: '/mail/mailboxes/forwarding' },
              { text: 'Signatures', link: '/mail/mailboxes/signatures' },
              { text: 'Users', link: '/mail/mailboxes/users' },
              {
                text: 'Accesses',
                collapsed: true,
                items: [
                  { text: 'Devices', link: '/mail/mailboxes/accesses/devices' },
                  { text: 'Invitations', link: '/mail/mailboxes/accesses/invitations' },
                  {
                    text: 'Webmail',
                    collapsed: true,
                    items: [
                      { text: 'Team', link: '/mail/mailboxes/accesses/webmail/team' },
                      { text: 'User', link: '/mail/mailboxes/accesses/webmail/user' },
                    ],
                  },
                ],
              },
              {
                text: 'Filters',
                collapsed: true,
                items: [
                  { text: 'Scripts', link: '/mail/mailboxes/filters/scripts' },
                ],
              },
              {
                text: 'Signatures',
                collapsed: true,
                items: [
                  { text: 'Templates', link: '/mail/mailboxes/signatures/templates' },
                ],
              },
            ],
          },
        ],
      },
      {
        text: 'Newsletter',
        link: '/newsletter/',
        collapsed: true,
        items: [
          { text: 'Credits', link: '/newsletter/credits' },
          { text: 'Dashboard', link: '/newsletter/dashboard' },
          { text: 'Domains', link: '/newsletter/domains' },
          { text: 'Fields', link: '/newsletter/fields' },
          { text: 'Operations', link: '/newsletter/operations' },
          {
            text: 'Campaigns',
            collapsed: true,
            items: [
              { text: 'Template', link: '/newsletter/campaigns/template' },
            ],
          },
          {
            text: 'Groups',
            collapsed: true,
            items: [
              { text: 'Subscribers', link: '/newsletter/groups/subscribers' },
            ],
          },
          {
            text: 'Segments',
            collapsed: true,
            items: [
              { text: 'Subscribers', link: '/newsletter/segments/subscribers' },
            ],
          },
          {
            text: 'Subscribers',
            collapsed: true,
            items: [
              { text: 'Addressbooks', link: '/newsletter/subscribers/addressbooks' },
            ],
          },
          {
            text: 'Templates',
            collapsed: true,
            items: [
              { text: 'Thumbnail', link: '/newsletter/templates/thumbnail' },
            ],
          },
          {
            text: 'Webforms',
            collapsed: true,
            items: [
              { text: 'Fields', link: '/newsletter/webforms/fields' },
              { text: 'Themes', link: '/newsletter/webforms/themes' },
            ],
          },
        ],
      },
      {
        text: 'Radio',
        link: '/radio/',
        collapsed: true,
        items: [
          { text: 'Encoder Events', link: '/radio/encoder_events' },
          { text: 'HLS Stream', link: '/radio/hls_stream' },
          { text: 'Mediapulse', link: '/radio/mediapulse' },
          { text: 'Notifications', link: '/radio/notifications' },
          { text: 'Options', link: '/radio/options' },
          { text: 'Packs', link: '/radio/packs' },
          { text: 'Product Options', link: '/radio/product_options' },
          { text: 'Server Events', link: '/radio/server_events' },
          {
            text: 'AutoDJ',
            collapsed: true,
            items: [
              { text: 'Events', link: '/radio/autodj/events' },
              { text: 'Media', link: '/radio/autodj/media' },
              {
                text: 'Playing Playlist',
                collapsed: true,
                items: [
                  { text: 'Medias', link: '/radio/autodj/playing_playlist/medias' },
                ],
              },
              {
                text: 'Playlists',
                collapsed: true,
                items: [
                  { text: 'Medias', link: '/radio/autodj/playlists/medias' },
                ],
              },
            ],
          },
          {
            text: 'Players',
            collapsed: true,
            items: [
              { text: 'Config', link: '/radio/players/config' },
              { text: 'Thumbnail', link: '/radio/players/thumbnail' },
            ],
          },
          {
            text: 'Products',
            collapsed: true,
            items: [
              { text: 'Conflict Restrictions', link: '/radio/products/conflict_restrictions' },
              { text: 'Restrictions', link: '/radio/products/restrictions' },
              { text: 'Users', link: '/radio/products/users' },
            ],
          },
          {
            text: 'Stats',
            collapsed: true,
            items: [
              { text: 'HLS Stream', link: '/radio/stats/hls_stream' },
              { text: 'Product', link: '/radio/stats/product' },
            ],
          },
        ],
      },
      {
        text: 'Tickets',
        link: '/tickets/',
        collapsed: true,
      },
      {
        text: 'URL',
        link: '/url/',
        collapsed: true,
        items: [
          { text: 'Short', link: '/url/short' },
        ],
      },
      {
        text: 'Video',
        link: '/video/',
        collapsed: true,
        items: [
          { text: 'Channel', link: '/video/channel' },
          { text: 'Countries', link: '/video/countries' },
          { text: 'Event', link: '/video/event' },
          { text: 'Integrations', link: '/video/integrations' },
          { text: 'Live', link: '/video/live' },
          { text: 'Order', link: '/video/order' },
          { text: 'Prices', link: '/video/prices' },
          { text: 'Restrictions', link: '/video/restrictions' },
          { text: 'Stream', link: '/video/stream' },
          { text: 'Thumbnail', link: '/video/thumbnail' },
          { text: 'Timezones', link: '/video/timezones' },
          {
            text: 'Options',
            collapsed: true,
            items: [
              {
                text: 'Record',
                collapsed: true,
                items: [
                  { text: 'Storage', link: '/video/options/record/storage' },
                ],
              },
              { text: 'Simulcast', link: '/video/options/simulcast' },
              { text: 'Timeshift', link: '/video/options/timeshift' },
              { text: 'Watermarking', link: '/video/options/watermarking' },
            ],
          },
          {
            text: 'Players',
            collapsed: true,
            items: [
              { text: 'Ads', link: '/video/players/ads' },
              { text: 'Embeds', link: '/video/players/embeds' },
              { text: 'Picture', link: '/video/players/picture' },
            ],
          },
          {
            text: 'Stats',
            collapsed: true,
            items: [
              { text: 'Channel', link: '/video/stats/channel' },
              { text: 'Geolocation', link: '/video/stats/geolocation' },
              { text: 'Globals', link: '/video/stats/globals' },
              { text: 'Viewers', link: '/video/stats/viewers' },
              { text: 'Viewing', link: '/video/stats/viewing' },
            ],
          },
        ],
      },
      {
        text: 'VOD',
        link: '/vod/',
        collapsed: true,
      },
    ],
    search: {
      provider: 'local',
    },
  },
})
