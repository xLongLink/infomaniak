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
        text: 'Cloud',
        link: '/cloud/',
        collapsed: true,
        items: [
          { text: 'Config', link: '/cloud/config' },
          { text: 'Projects', link: '/cloud/projects' },
          {
            text: 'Database',
            link: '/cloud/database/',
            items: [
              { text: 'Overview', link: '/cloud/database/' },
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
            link: '/cloud/kubernetes/',
            items: [
              { text: 'Overview', link: '/cloud/kubernetes/' },
              { text: 'Data', link: '/cloud/kubernetes/data' },
              { text: 'IP', link: '/cloud/kubernetes/ip' },
              { text: 'Pools', link: '/cloud/kubernetes/pools' },
            ],
          },
        ],
      },
      { text: 'DNS', link: '/dns/', collapsed: true, items: [{ text: 'Domain', link: '/dns/domain' }, { text: 'Top Level Domain', link: '/dns/tld' }, { text: 'Zone', link: '/dns/zone' }] },
    ],
    search: {
      provider: 'local',
    },
  },
})
