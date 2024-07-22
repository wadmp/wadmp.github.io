import store from "../store";
import { EventBus } from "../eventBus.js";

export default {
  watch: {
    $route(to, from) {
      this.detectVersionFromURL(to.path);
    },
  },
  mounted() {
    this.detectVersionFromURL(this.$route.path);
  },
  methods: {
    detectVersionFromURL(path) {
      const version = path.includes("/gen2/")
        ? "Version 2.x.x"
        : "Version 3.x.x";
      if (version !== store.state.version) {
        store.mutations.setVersion(version);
        this.$router.app.$emit("version-changed", version);
      }
    },
  },
};
