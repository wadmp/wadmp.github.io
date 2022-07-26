const { description } = require('../../package')

module.exports = {
  base: "/newdocs.wadmp.github.io/",
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#title
   */
  title: 'WebAccess/DMP Documentation',
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#description
   */
  description: description,
  
  /**
   * Extra tags to be injected to the page HTML `<head>`
   *
   * ref：https://v1.vuepress.vuejs.org/config/#head
   */
  head: [
    ['meta', { name: 'theme-color', content: '#3eaf7c' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }],
    /* ['link', {
      rel: 'stylesheet',
      href: `https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css`
    }],
    ['script', { src: `https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js` }],
    ['script', { src: `https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js` }], */
  ],
  dest: 'docs',
  /**
   * Theme configuration, here is the default theme configuration for VuePress.
   *
   * ref：https://v1.vuepress.vuejs.org/theme/default-theme-config.html
   */
  themeConfig: {
    logo: '/assets/img/logo.png',
    repo: '',
    docsDir: '',
    lastUpdated: true,
    nav: [
      {
        text: 'Tutorials',
        link: '/tutorials/',
      },
      {
        text: 'Explanations',
        link: '/explanations/'
      },
      {
        text: 'Release Notes',
        link: '/release-notes/'
      },
      {
        text: 'Client Release Notes',
        link: '/client/'
      },      
      {
        text: 'Support & Contact',
        link: '/contact/'
      }
    ],
    sidebar: {
      '/tutorials/': [
        '',     /* /README.md/ */
        'ui-general-structure/',   /* README.md */
        'create-company/',   /* README.md */
        'create-users/',   /* README.md */
        'device/',   /* README.md */
        'search-filter-devices/',   /* README.md */
        'configuring-router-apps/',   /* README.md */
        'configuring-on_off-devices/',   /* README.md */
        'upgrade-fw/',   /* README.md */
        'move-a-device/'   /* README.md */
      ],
      '/explanations/': [
        '',      /* /README.md/ */
        'companies-and-users/',  /* /README.md */
        'understanding-oauth/',  /* /README.md */
        'cellular-data-usage/',  /* /README.md */
        'grouping-and-tagging/',  /* /README.md */
        'billing/',  /* /README.md */
        'playbooks/',  /* /README.md */
        'grafana/',  /* /README.md */
        'alerts/',  /* /README.md */
        'auditing-options/',  /* /README.md */
        // 'gen1-to-gen2-migration/',  /* /README.md */
        'cant-connect-my-device/',  /* /README.md */
        'adding-or-claiming-devices-in-bulk/'  /* /README.md */

      ],
      '/release-notes/': [
        '',      /* /README.md/ */
        '2.4.2/',      /* /README.md/ */
        '2.4.1/',  /* /2.4.1.md */
        '2.4.0/',  /* /2.4.0.md */
        '2.3.1/',  /* /2.3.1.md */
        '2.3.0/',  /* /2.3.0.md */
        '2.2.0/',  /* /2.2.0.md */
        '2.1.1/',  /* /2.1.1.md */
        '2.1.0/'  /* /2.1.0.md */
      ],
      '/contact/': [
      ],
      '/client/': [
      ],
      '/eula': [
      ],
      '/privacy-policy': [
      ]
    },
    sidebarDepth: 5,
    // Optional options for generating "Edit this page" link
    // if your docs are in a different repo from your main project:
    docsRepo: 'wadmp/wadmp.github.io',
    // if your docs are not at the root of the repo:
    // docsDir: 'docs',
    // if your docs are in a specific branch (defaults to 'master'):
    // defaults to false, set to true to enable
    editLinks: true,
    // custom text for edit link. Defaults to "Edit this page"
    editLinkText: 'Help us improve this page!'
  },

  /**
   * Apply plugins，ref：https://v1.vuepress.vuejs.org/zh/plugin/
   */
  plugins: [
    '@vuepress/plugin-back-to-top',
    '@vuepress/plugin-medium-zoom',
  ]
}
