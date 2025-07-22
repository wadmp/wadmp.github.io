const { description } = require("../../package");
const path = require("path");
const { getVersionedNav } = require("./utils/getVersionedNav");

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
    // lastUpdated: true,
    nav: getVersionedNav("Version 3.x.x"), // Default version nav
    sidebar: {  
      "/gen3/docs/": [
        {
          title: "User Management", // required
          path: "/gen3/docs/", // optional, link of the title, which should be an absolute path and must exist
          collapsable: false, // optional, defaults to true
          sidebarDepth: 0, // optional, defaults to 1
          children: [
            "/gen3/docs/user-management/sign-up/",
            "/gen3/docs/user-management/add-users/",
            "/gen3/docs/user-management/remove-users/",
            "/gen3/docs/user-management/2fa/",
            "/gen3/docs/user-management/permissions/",
          ],
        },

        {
          title: "Companies",
          path: "/gen3/docs/companies/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/companies/company-structure/",
            "/gen3/docs/companies/audit-logs/",
            "/gen3/docs/companies/premium-features/",
            "/gen3/docs/companies/billing/",
          ],
        },

        {
          title: "Adding Devices",
          path: "/gen3/docs/adding-devices/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/adding-devices/register-a-device/",
            "/gen3/docs/adding-devices/add-a-device/",
            "/gen3/docs/adding-devices/install-client-app/",
          ],
        },
        {
          title: "Device Management",
          path: "/gen3/docs/device-management/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/device-management/dmp-client-app/",
            "/gen3/docs/device-management/fields/",
            "/gen3/docs/device-management/device-configuration/",
            "/gen3/docs/device-management/csv-import-guide/",
          ],
        },
        {
          title: "Device Monitoring",
          path: "/gen3/docs/device-monitoring/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/device-monitoring/collecting-data/",
            "/gen3/docs/device-monitoring/exporting-data-to-csv/",
          ],
        },
        {
          title: "Dashboards & Widgets",
          path: "/gen3/docs/dashboards-widgets/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/dashboards-widgets/customization-of-views/",
            "/gen3/docs/dashboards-widgets/tips-tricks/",
          ],
        },
        {
          title: "VPN",
          path: "/gen3/docs/vpn/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/vpn/overview/",
            "/gen3/docs/vpn/networks/",
            "/gen3/docs/vpn/roadwarriors/",
          ],
        },
        {
          title: "Alerts",
          path: "/gen3/docs/alerts/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/alerts/creating-new-alerts/",
            "/gen3/docs/alerts/alerting-limitations/",
          ],
        },
        //{
        //  title: "API",
        //  path: "/gen3/docs/api/",
        //  collapsable: true,
        // sidebarDepth: 1,
        //},

        {
          title: "Troubleshooting",
          path: "/gen3/docs/troubleshooting/",
          collapsable: false,
          sidebarDepth: 0,
        },

        {
          title: "FAQ",
          path: "/gen3/docs/faq/",
          collapsable: false,
          sidebarDepth: 0,
        },
        {
          title: "Migration from 2.x.x to 3.x.x Instance",
          path: "/gen3/docs/migration/",
          collapsable: false,
          sidebarDepth: 0,
        },
      ],
      "/gen3/api/": [
        {
          title: "Overview", // required
          path: "/gen3/api/", // optional, link of the title, which should be an absolute path and must exist
          collapsable: false, // optional, defaults to true
          sidebarDepth: 0, // optional, defaults to 1
          children: []
        },
        {
          title: "Authentication",
          path: "/gen3/api/authentication/",
          collapsable: false,
          sidebarDepth: 0,
          children: []
        },
        {
          title: "Getting Started",
          path: "/gen3/api/getting-started/",
          collapsable: false,
          sidebarDepth: 0,
          children: []
        },
        {
          title: "Useful Examples",
          path: "/gen3/api/useful-examples/",
          collapsable: false,
          sidebarDepth: 0,
          children: []
        }
      ],
      "/gen3/release-notes/": [
        "" /* /README.md/ */,
        "3.2.0/" /* /README.md/ */,
        "3.1.2/" /* /README.md/ */,
        "3.1.1/" /* /README.md/ */,
        "3.1.0/" /* /README.md/ */,
        "3.0.3/" /* /README.md/ */,
        "3.0.2/" /* /README.md/ */,
        "3.0.1/" /* /README.md/ */,
        "3.0.0/" /* /README.md/ */,
      ],
      "/contact/": [],
      "/gen3/client/": [],
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
    // editLinks: true,
    // custom text for edit link. Defaults to "Edit this page"
    // editLinkText: "Help us improve this page!",
  },

  /**
   * Apply plugins，ref：https://v1.vuepress.vuejs.org/zh/plugin/
   */
  plugins: [
    [
      "@vuepress/plugin-back-to-top",
      "@vuepress/plugin-medium-zoom",
      "@vuepress/plugin-register-components",
    ],
    {
      components: [
        {
          name: "VersionSwitcher",
          path: path.resolve(__dirname, "./components/VersionSwitcher.vue"),
        },
      ],
    },
    path.resolve(__dirname, "./plugins/versionSwitcherPlugin.js"),
  ],
};
