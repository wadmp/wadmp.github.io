import { EventBus } from "../eventBus.js";
import { getVersionedNav } from "../utils/getVersionedNav.js";
import store from "../store";

export default {
  mounted() {
    const savedVersion = store.state.version || "Version 3.x.x";
    this.updateNav(savedVersion);

    // Listen for version changes
    EventBus.$on("version-changed", (version) => {
      this.updateNav(version);
    });
  },
  methods: {
    updateNav(version) {
      this.$site.themeConfig.nav = getVersionedNav(version);
      // Ensure VuePress re-renders with the new navigation config
      this.$router.app.$emit("nav-updated");
    },
  },
};
