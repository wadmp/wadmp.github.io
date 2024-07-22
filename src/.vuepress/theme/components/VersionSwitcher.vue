<template>
  <div class="version-switcher">
    <select @change="switchVersion" v-model="$store.state.version">
      <option v-for="version in versions" :key="version" :value="version">
        {{ version }}
      </option>
    </select>
  </div>
</template>

<script>
import { EventBus } from "../../eventBus.js";
import { getVersionedNav } from "../../utils/getVersionedNav.js";

export default {
  computed: {
    versions() {
      return ["Version 3.x.x", "Version 2.x.x"];
    },
    currentVersion() {
      return this.$store.state.version;
    },
  },
  methods: {
    switchVersion(event) {
      const selectedVersion = event.target.value;
      this.$store.mutations.setVersion(selectedVersion);
      // Emit an event to notify other components of the version change
      EventBus.$emit("version-changed", selectedVersion);

      switch (selectedVersion) {
        case "Version 3.x.x":
          this.$router.push(`/gen3/`);
          break;
        case "Version 2.x.x":
          this.$router.push(`/gen2/`);
          break;
        default:
        // code block
      }
      this.updateNav(selectedVersion); // Update navigation
    },
    updateNav(version) {
      this.$site.themeConfig.nav = getVersionedNav(version);
      this.$router.app.$emit("nav-updated"); // Emit event to force re-render
    },
  },
};
</script>

<style>
.version-switcher {
  margin-right: 20px;
  margin-left: 20px;
}
.version-switcher select {
  height: 2rem;
  display: inline-block;
  border: 1px solid #cfd4db;
  border-radius: 2rem;
  font-size: 0.9rem;
  font-weight: 600;
  line-height: 2rem;
  padding: 0 0.5rem 0 0.7rem;
  outline: none;
  transition: all 0.2s ease;
  background: #fff;
}
</style>
