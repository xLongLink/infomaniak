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
        collapsed: true,
        items: [{ text: 'Overview', link: '/ai/' }],
      },
      {
        text: 'Backup',
        collapsed: true,
        items: [
          { text: 'Overview', link: '/backup/' },
          { text: 'Administrator', link: '/backup/administrator' },
          { text: 'Billing', link: '/backup/billing' },
          { text: 'Passwords', link: '/backup/passwords' },
          { text: 'Product', link: '/backup/product' },
          { text: 'Slots', link: '/backup/slots' },
        ],
      },
      {
        text: 'Cloud',
        collapsed: true,
        items: [
          { text: 'Overview', link: '/cloud/' },
          {
            text: 'Database',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/cloud/database' },
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
              { text: 'Overview', link: '/cloud/kubernetes' },
              { text: 'Data', link: '/cloud/kubernetes/data' },
              { text: 'IP', link: '/cloud/kubernetes/ip' },
              { text: 'Pools', link: '/cloud/kubernetes/pools' },
            ],
          },
        ],
      },
      {
        text: 'Core',
        collapsed: true,
        items: [
          { text: 'Overview', link: '/core/' },
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
              { text: 'Overview', link: '/core/ksuite' },
              { text: 'Mailbox', link: '/core/ksuite/mailbox' },
            ],
          },
          {
            text: 'Profile',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/core/profile' },
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
              { text: 'Overview', link: '/core/user' },
              { text: 'Accounts', link: '/core/user/accounts' },
              { text: 'Teams', link: '/core/user/teams' },
            ],
          },
        ],
      },
      {
        text: 'DNS',
        collapsed: true,
        items: [{ text: 'Overview', link: '/dns/' }],
      },
      {
        text: 'Domain',
        collapsed: true,
        items: [
          { text: 'Overview', link: '/domain/' },
          { text: 'DNSSEC', link: '/domain/dnssec' },
          { text: 'Nameservers', link: '/domain/nameservers' },
          { text: 'Order', link: '/domain/order' },
          { text: 'Zone', link: '/domain/zone' },
        ],
      },
      {
        text: 'kChat',
        collapsed: true,
        items: [
          { text: 'Overview', link: '/kchat/' },
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
        text: 'kDrive',
        collapsed: true,
        items: [{ text: 'Overview', link: '/kdrive/' }],
      },
      {
        text: 'kMeet',
        collapsed: true,
        items: [
          { text: 'Overview', link: '/kmeet/' },
          { text: 'Plan', link: '/kmeet/plan' },
          { text: 'Room', link: '/kmeet/room' },
        ],
      },
      {
        text: 'Mail',
        collapsed: true,
        items: [{ text: 'Overview', link: '/mail/' }],
      },
      {
        text: 'Newsletter',
        collapsed: true,
        items: [
          { text: 'Overview', link: '/newsletter/' },
          { text: 'Credits', link: '/newsletter/credits' },
          { text: 'Dashboard', link: '/newsletter/dashboard' },
          { text: 'Domains', link: '/newsletter/domains' },
          { text: 'Fields', link: '/newsletter/fields' },
          { text: 'Operations', link: '/newsletter/operations' },
          {
            text: 'Campaigns',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/newsletter/campaigns' },
              { text: 'Template', link: '/newsletter/campaigns/template' },
            ],
          },
          {
            text: 'Groups',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/newsletter/groups' },
              { text: 'Subscribers', link: '/newsletter/groups/subscribers' },
            ],
          },
          {
            text: 'Segments',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/newsletter/segments' },
              { text: 'Subscribers', link: '/newsletter/segments/subscribers' },
            ],
          },
          {
            text: 'Subscribers',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/newsletter/subscribers' },
              { text: 'Addressbooks', link: '/newsletter/subscribers/addressbooks' },
            ],
          },
          {
            text: 'Templates',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/newsletter/templates' },
              { text: 'Thumbnail', link: '/newsletter/templates/thumbnail' },
            ],
          },
          {
            text: 'Webforms',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/newsletter/webforms' },
              { text: 'Fields', link: '/newsletter/webforms/fields' },
              { text: 'Themes', link: '/newsletter/webforms/themes' },
            ],
          },
        ],
      },
      {
        text: 'Radio',
        collapsed: true,
        items: [
          { text: 'Overview', link: '/radio/' },
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
              { text: 'Overview', link: '/radio/autodj' },
              { text: 'Events', link: '/radio/autodj/events' },
              { text: 'Media', link: '/radio/autodj/media' },
              {
                text: 'Playing Playlist',
                collapsed: true,
                items: [
                  { text: 'Overview', link: '/radio/autodj/playing_playlist' },
                  { text: 'Medias', link: '/radio/autodj/playing_playlist/medias' },
                ],
              },
              {
                text: 'Playlists',
                collapsed: true,
                items: [
                  { text: 'Overview', link: '/radio/autodj/playlists' },
                  { text: 'Medias', link: '/radio/autodj/playlists/medias' },
                ],
              },
            ],
          },
          {
            text: 'Players',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/radio/players' },
              { text: 'Config', link: '/radio/players/config' },
              { text: 'Thumbnail', link: '/radio/players/thumbnail' },
            ],
          },
          {
            text: 'Products',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/radio/products' },
              { text: 'Conflict Restrictions', link: '/radio/products/conflict_restrictions' },
              { text: 'Restrictions', link: '/radio/products/restrictions' },
              { text: 'Users', link: '/radio/products/users' },
            ],
          },
          {
            text: 'Stats',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/radio/stats' },
              { text: 'HLS Stream', link: '/radio/stats/hls_stream' },
              { text: 'Product', link: '/radio/stats/product' },
            ],
          },
        ],
      },
      {
        text: 'Tickets',
        collapsed: true,
        items: [{ text: 'Overview', link: '/tickets/' }],
      },
      {
        text: 'URL',
        collapsed: true,
        items: [
          { text: 'Overview', link: '/url/' },
          { text: 'Short', link: '/url/short' },
        ],
      },
      {
        text: 'Video',
        collapsed: true,
        items: [
          { text: 'Overview', link: '/video/' },
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
              { text: 'Overview', link: '/video/options' },
              {
                text: 'Record',
                collapsed: true,
                items: [
                  { text: 'Overview', link: '/video/options/record' },
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
              { text: 'Overview', link: '/video/players' },
              { text: 'Ads', link: '/video/players/ads' },
              { text: 'Embeds', link: '/video/players/embeds' },
              { text: 'Picture', link: '/video/players/picture' },
            ],
          },
          {
            text: 'Stats',
            collapsed: true,
            items: [
              { text: 'Overview', link: '/video/stats' },
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
        collapsed: true,
        items: [{ text: 'Overview', link: '/vod/' }],
      },
    ],
    search: {
      provider: 'local',
    },
  },
})
