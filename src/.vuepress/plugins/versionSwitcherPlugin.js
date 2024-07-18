const { path } = require("@vuepress/shared-utils");

module.exports = (options, ctx) => ({
  name: "version-switcher-plugin",
  clientRootMixin: path.resolve(__dirname, "versionSwitcherClientMixin.js"),
});
