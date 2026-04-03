import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Infomaniak SDK for Python',
  description: 'Python SDK documentation for the Infomaniak API.',
  srcDir: 'src',
  base: process.env.NODE_ENV === 'production' ? '/infomaniak/' : '/',
  cleanUrls: true,
  themeConfig: {
    sidebar: [
      {
        text: 'AI',
        collapsed: true,
        items: [{ text: 'Overview', link: '/ai/' }],
      },
      {
        text: 'Backup',
        collapsed: true,
        items: [{ text: 'Overview', link: '/backup/' }],
      },
      {
        text: 'Cloud',
        collapsed: true,
        items: [{ text: 'Overview', link: '/cloud/' }],
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
          { text: 'Profile', link: '/core/profile' },
          { text: 'User', link: '/core/user' },
          { text: 'User Accounts', link: '/core/user/acccounts' },
          { text: 'User Teams', link: '/core/user/teams' },
        ],
      },
      {
        text: 'DNS',
        collapsed: true,
        items: [{ text: 'Overview', link: '/dns/' }],
      },
      {
        text: 'kChat',
        collapsed: true,
        items: [
          { text: 'Overview', link: '/kchat/' },
          { text: 'Users', link: '/kchat/users' },
          { text: 'Bots', link: '/kchat/bots' },
          { text: 'Teams', link: '/kchat/teams' },
          { text: 'Channels', link: '/kchat/channels' },
          { text: 'Posts', link: '/kchat/posts' },
          { text: 'Threads', link: '/kchat/threads' },
          { text: 'Files', link: '/kchat/files' },
          { text: 'Preferences', link: '/kchat/preferences' },
          { text: 'Status', link: '/kchat/status' },
          { text: 'Emoji', link: '/kchat/emoji' },
          { text: 'Reactions', link: '/kchat/reactions' },
          { text: 'Webhooks', link: '/kchat/webhooks' },
          { text: 'Commands', link: '/kchat/commands' },
          { text: 'System', link: '/kchat/system' },
          { text: 'Groups', link: '/kchat/groups' },
          { text: 'Roles', link: '/kchat/roles' },
          { text: 'Insights', link: '/kchat/insights' },
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
        items: [{ text: 'Overview', link: '/newsletter/' }],
      },
      {
        text: 'Radio',
        collapsed: true,
        items: [{ text: 'Overview', link: '/radio/' }],
      },
      {
        text: 'Tickets',
        collapsed: true,
        items: [{ text: 'Overview', link: '/tickets/' }],
      },
      {
        text: 'URL',
        collapsed: true,
        items: [{ text: 'Overview', link: '/url/' }],
      },
      {
        text: 'Video',
        collapsed: true,
        items: [{ text: 'Overview', link: '/video/' }],
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
