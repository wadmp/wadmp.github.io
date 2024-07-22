import Vue from "vue";

const state = Vue.observable({
  version: "Version 3.x.x", // Default version
});

const mutations = {
  setVersion(version) {
    state.version = version;
  },
};

export default {
  state,
  mutations,
};
