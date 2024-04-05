const { description } = require("../../package");

module.exports = {
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#title
   */
  title: "WebAccess/DMP Documentation",
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
    ["meta", { name: "theme-color", content: "#3eaf7c" }],
    ["meta", { name: "apple-mobile-web-app-capable", content: "yes" }],
    [
      "meta",
      { name: "apple-mobile-web-app-status-bar-style", content: "black" },
    ],
    /* ['link', {
      rel: 'stylesheet',
      href: `https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.min.css`
    }],
    ['script', { src: `https://cdn.jsdelivr.net/npm/vue@2.x/dist/vue.js` }],
    ['script', { src: `https://cdn.jsdelivr.net/npm/vuetify@2.x/dist/vuetify.js` }], */
  ],
  dest: "docs",
  /**
   * Theme configuration, here is the default theme configuration for VuePress.
   *
   * ref：https://v1.vuepress.vuejs.org/theme/default-theme-config.html
   */
  themeConfig: {
    logo: "/assets/img/logo.png",
    repo: "",
    docsDir: "",
    lastUpdated: true,
    nav: [
      {
        text: "Tutorials",
        ariaLabel: "Tutorials",
        items: [
          { text: "Version 3.x.x", link: "/gen3/tutorials/" },
          { text: "Version 2.x.x", link: "/gen2/tutorials/" },
          {
            text: "Migration 2.x.x to 3.x.x",
            link: "/gen3/tutorials/migration-gen2-gen3/",
          },
        ],
      },
      {
        text: "Explanations",
        ariaLabel: "Explanations",
        items: [
          { text: "Version 3.x.x", link: "/gen3/explanations/" },
          { text: "Version 2.x.x", link: "/gen2/explanations/" },
        ],
      },
      {
        text: "Release Notes (Server)",
        ariaLabel: "Release Notes (Server)",
        items: [
          { text: "Version 3.x.x", link: "/gen3/release-notes/" },
          { text: "Version 2.x.x", link: "/gen2/release-notes/" },
        ],
      },
      {
        text: "Release Notes (Client)",
        ariaLabel: "Release Notes (Client)",
        items: [
          { text: "Version 3.x.x", link: "/gen3/client/" },
          { text: "Version 2.x.x", link: "/gen2/client/" },
        ],
      },
      {
        text: "Support & Contact",
        link: "/contact/",
      },
    ],
    sidebar: {
      "/gen3/tutorials/": [
        "" /* /README.md/ */,
        "ui-general-structure/" /* README.md */,
        "create-company/" /* README.md */,
        "migration-gen2-gen3/" /* README.md */,
        "create-users/" /* README.md */,
        "invite-existing-or-new-user/" /* README.md */,
        "device/" /* README.md */,
        "search-filter-devices/" /* README.md */,
        "config-profiles/" /* README.md */,
      ],
      "/gen2/tutorials/": [
        "" /* /README.md/ */,
        "ui-general-structure/" /* README.md */,
        "create-company/" /* README.md */,
        "create-users/" /* README.md */,
        "device/" /* README.md */,
        "search-filter-devices/" /* README.md */,
        "configuring-router-apps/" /* README.md */,
        "configuring-on_off-devices/" /* README.md */,
        "upgrade-fw/" /* README.md */,
        "move-a-device/" /* README.md */,
      ],
      "/gen3/explanations/": [
        "" /* /README.md/ */,
        "companies/" /* /README.md */,
        "adding devices/" /* /README.md */,
        "device management/" /* /README.md */,
        "device monitoring/" /* /README.md */,
        "dashboards & Widgets/" /* /README.md */,
        "alerts/" /* /README.md */,
        "api/" /* /README.md */,
        "troubleshooting/" /* /README.md */,
        "Migration from 2.x.x to 3.x.x instance/" /* /README.md */,
      
      ],
      "/gen2/explanations/": [
        "" /* /README.md/ */,
        "companies-and-users/" /* /README.md */,
        "permissions/" /* /README.md */,
        "cellular-data-usage/" /* /README.md */,
        "grouping-and-tagging/" /* /README.md */,
        "billing/" /* /README.md */,
        "playbooks/" /* /README.md */,
        "grafana/" /* /README.md */,
        "alerts/" /* /README.md */,
        "2fa/" /* /README.md */,
        "auditing-options/" /* /README.md */,
        // 'gen1-to-gen2-migration/',  /* /README.md */
        "cant-connect-my-device/" /* /README.md */,
        "adding-or-claiming-devices-in-bulk/" /* /README.md */,
        "bunch-claiming-devices/" /* /README.md */,
        "wadmp-ports/" /* /README.md */,
      ],
      "/gen3/release-notes/": [
        "" /* /README.md/ */,
        "3.0.2/" /* /README.md/ */,
        "3.0.1/" /* /README.md/ */,
        "3.0.0/" /* /README.md/ */,
      ],
      "/gen2/release-notes/": [
        "" /* /README.md/ */,
        "2.5.4/" /* /README.md/ */,
        "2.5.3/" /* /README.md/ */,
        "2.5.2/" /* /README.md/ */,
        "2.5.1/" /* /README.md/ */,
        "2.5.0/" /* /README.md/ */,
        "2.4.4/" /* /README.md/ */,
        "2.4.3/" /* /README.md/ */,
        "2.4.2/" /* /README.md/ */,
        "2.4.1/" /* /2.4.1.md */,
        "2.4.0/" /* /2.4.0.md */,
        "2.3.1/" /* /2.3.1.md */,
        "2.3.0/" /* /2.3.0.md */,
        "2.2.0/" /* /2.2.0.md */,
        "2.1.1/" /* /2.1.1.md */,
        "2.1.0/" /* /2.1.0.md */,
      ],
      "/contact/": [],
      "/gen3/client/": [],
      "/gen2/client/": [],
      "/eula": [],
      "/privacy-policy": [],
    },
    sidebarDepth: 5,
    // Optional options for generating "Edit this page" link
    // if your docs are in a different repo from your main project:
    docsRepo: "wadmp/wadmp.github.io",
    // if your docs are not at the root of the repo:
    // docsDir: 'docs',
    // if your docs are in a specific branch (defaults to 'master'):
    // defaults to false, set to true to enable
    editLinks: true,
    // custom text for edit link. Defaults to "Edit this page"
    editLinkText: "Help us improve this page!",
  },

  /**
   * Apply plugins，ref：https://v1.vuepress.vuejs.org/zh/plugin/
   */
  plugins: ["@vuepress/plugin-back-to-top", "@vuepress/plugin-medium-zoom"],
};
