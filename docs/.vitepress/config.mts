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
      { text: 'Cloud', link: '/cloud/', collapsed: true, items: [{ text: 'Projects', link: '/cloud/projects' }] },
      { text: 'DNS', link: '/dns/', collapsed: true, items: [{ text: 'Domain', link: '/dns/domain' }, { text: 'Top Level Domain', link: '/dns/tld' }, { text: 'Zone', link: '/dns/zone' }] },
    ],
    search: {
      provider: 'local',
    },
  },
})
