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
        text: 'Overview',
        link: '/',
        collapsed: false
      },
      {
        text: 'Pagination',
        link: '/pagination',
        collapsed: false
      },
      {
        text: 'Cloud',
        collapsed: true,
        items: [
          { text: 'Index', link: '/cloud/' },
          { text: 'Config', link: '/cloud/config' },
          { text: 'Projects', link: '/cloud/projects' },
          {
            text: 'Database',
            collapsed: true,
            items: [
              { text: 'Index', link: '/cloud/database/' },
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
              { text: 'Index', link: '/cloud/kubernetes/' },
              { text: 'Data', link: '/cloud/kubernetes/data' },
              { text: 'IP', link: '/cloud/kubernetes/ip' },
              { text: 'Pools', link: '/cloud/kubernetes/pools' },
            ],
          },
        ],
      },
      {
        text: 'DNS', link: '/dns/', collapsed: true, items: [
          { text: 'Domain', link: '/dns/domain' },
          { text: 'Top Level Domain', link: '/dns/tld' },
          { text: 'Zone', link: '/dns/zone' }
        ]
      },
      {
        text: 'Core',
        collapsed: true,
        items: [
          { text: 'Timezones', link: '/core/timezones' },
        ],
      },
      {
        text: 'Tasks',
        link: '/tasks',
        collapsed: false
      },
    ],
    search: {
      provider: 'local',
    },
  },
})
