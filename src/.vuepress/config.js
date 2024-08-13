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
    lastUpdated: true,
    nav: getVersionedNav("Version 3.x.x"), // Default version nav
    sidebar: {
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

          themeConfig: {
            // default value is true. Set it to false to hide next page links on all pages
            nextLinks: true,
            // default value is true. Set it to false to hide prev page links on all pages
            prevLinks: true
          }
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
          themeConfig: {
            // default value is true. Set it to false to hide next page links on all pages
            nextLinks: true,
            // default value is true. Set it to false to hide prev page links on all pages
            prevLinks: true
          }
        },

        {
          title: "Adding devices",
          path: "/gen3/docs/adding devices/register-a-device/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/adding devices/register-a-device/",
            "/gen3/docs/adding devices/add-a-device/",
            "/gen3/docs/adding devices/install-client-app/",
          ],
          themeConfig: {
            // default value is true. Set it to false to hide next page links on all pages
            nextLinks: true,
            // default value is true. Set it to false to hide prev page links on all pages
            prevLinks: true
          }
        },
        {
          title: "Device management",
          path: "/gen3/docs/device management/dmp-client-app/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/device management/dmp-client-app/",
            "/gen3/docs/device management/fields/",
            "/gen3/docs/device management/device-configuration/",

          ],
          themeConfig: {
            // default value is true. Set it to false to hide next page links on all pages
            nextLinks: true,
            // default value is true. Set it to false to hide prev page links on all pages
            prevLinks: true
          }
        },
        {
          title: "Device monitoring",
          path: "/gen3/docs/device monitoring/collecting-data/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/device monitoring/collecting-data/",
            "/gen3/docs/device monitoring/exporting-data-to-csv/",

          ],
          themeConfig: {
            // default value is true. Set it to false to hide next page links on all pages
            nextLinks: true,
            // default value is true. Set it to false to hide prev page links on all pages
            prevLinks: true
          }
        },
        {
          title: "Dashboards & Widgets",
          path: "/gen3/docs/dashboards & Widgets/customization-of-views/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/dashboards & Widgets/customization-of-views/",
            "/gen3/docs/dashboards & Widgets/tips-tricks/",

          ],
          themeConfig: {
            // default value is true. Set it to false to hide next page links on all pages
            nextLinks: true,
            // default value is true. Set it to false to hide prev page links on all pages
            prevLinks: true
          }
        },
        
        {
          title: "Alerts",
          path: "/gen3/docs/alerts/creating-new-alerts/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/alerts/creating-new-alerts/",
            "/gen3/docs/alerts/alerting-limitations/",

          ],
          themeConfig: {
            // default value is true. Set it to false to hide next page links on all pages
            nextLinks: true,
            // default value is true. Set it to false to hide prev page links on all pages
            prevLinks: true
          }
        },

        {
          title: "Api",
          path: "/gen3/docs/api/use-dmp-from-swagger/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/api/use-dmp-from-swagger/",
            "/gen3/docs/api/configuration-using-api/",
            "/gen3/docs/api/bunch-claiming-using-script/",
          ],
          themeConfig: {
            // default value is true. Set it to false to hide next page links on all pages
            nextLinks: true,
            // default value is true. Set it to false to hide prev page links on all pages
            prevLinks: true
          }
        },


        {
          title: "Troubleshooting",
          path: "/gen3/docs/troubleshooting/scenario1/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/troubleshooting/scenario1/",
          ],
          themeConfig: {
            // default value is true. Set it to false to hide next page links on all pages
            nextLinks: true,
            // default value is true. Set it to false to hide prev page links on all pages
            prevLinks: true
          }
        },


        {
          title: "FAQ",
          path: "/gen3/docs/faq/list-of-adresses-and-ports/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/faq/list-of-adresses-and-ports/",
          ],
          themeConfig: {
            // default value is true. Set it to false to hide next page links on all pages
            nextLinks: true,
            // default value is true. Set it to false to hide prev page links on all pages
            prevLinks: true
          }
        },
        {
          title: "Migration from 2.x.x to 3.x.x instance",
          path: "/gen3/docs/Migration from 2.x.x to 3.x.x instance/steps/",
          collapsable: false,
          sidebarDepth: 0,
          children: [
            "/gen3/docs/Migration from 2.x.x to 3.x.x instance/steps/",
          ],
          themeConfig: {
            // default value is true. Set it to false to hide next page links on all pages
            nextLinks: true,
            // default value is true. Set it to false to hide prev page links on all pages
            prevLinks: true
          }
        },
      ],


      
      /*
      "/gen3/explanations/": [
        "" ,
        "companies/" ,
        "adding devices/" ,
        "device management/" ,
        "device monitoring/" ,
        "dashboards & Widgets/" ,
        "alerts/" ,
        "api/" ,
        "troubleshooting/" ,
        "faq/" /* ,
        "Migration from 2.x.x to 3.x.x instance/" ,
      ],
      */
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
        "Migration from 2.x.x to 3.x.x instance/" /* /README.md */,
      ],
      "/gen3/release-notes/": [
        "" /* /README.md/ */,
        "3.0.3/" /* /README.md/ */,
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
