import { defineConfig } from 'vitepress'

const repositoryName = process.env.GITHUB_REPOSITORY?.split('/')[1]
const base = process.env.GITHUB_ACTIONS === 'true' && repositoryName ? `/${repositoryName}/` : '/'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  base,
  title: "Infomaniak Python SDK",
  description: "Unofficial Infomaniak Python SDK",
  srcDir: 'src',
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    sidebar: [
      {
        text: 'Core',
        items: [
          { text: 'Overview', link: '/core/' },
          { text: 'Actions', link: '/core/actions' },
          { text: 'Countries', link: '/core/countries' },
          { text: 'Events', link: '/core/events' },
          { text: 'Languages', link: '/core/languages' },
          { text: 'Profile', link: '/core/profile' },
          {
            text: 'User',
            collapsed: false,
            items: [
              { text: 'Overview', link: '/core/user' },
              { text: 'Acccounts', link: '/core/user/acccounts' },
              { text: 'Teams', link: '/core/user/teams' }
            ]
          }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/XLongLink/infomaniak' }
    ]
  }
})
