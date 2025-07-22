<template>
  <header class="navbar" :key="navbarKey">
    <SidebarButton @toggle-sidebar="$emit('toggle-sidebar')" />
    <RouterLink :to="homeLink()" class="home-link">
      <img
        v-if="$site.themeConfig.logo"
        class="logo"
        :src="$withBase($site.themeConfig.logo)"
        :alt="$siteTitle"
      />
      <span
        v-if="$siteTitle"
        ref="siteName"
        class="site-name"
        :class="{ 'can-hide': $site.themeConfig.logo }"
      >
        Documentation
      </span>
    </RouterLink>

    <div
      class="links"
      :style="
        linksWrapMaxWidth
          ? {
              'max-width': linksWrapMaxWidth + 'px',
            }
          : {}
      "
    >
      <AlgoliaSearchBox v-if="isAlgoliaSearch" :options="algolia" />
      <SearchBox
        v-else-if="
          $site.themeConfig.search !== false &&
          $page.frontmatter.search !== false
        "
      />
      <VersionSwitcher />
      <NavLinks class="can-hide" />
    </div>
  </header>
</template>

<script>
import AlgoliaSearchBox from "@AlgoliaSearchBox";
import SearchBox from "@SearchBox";
import SidebarButton from "@theme/components/SidebarButton.vue";
import NavLinks from "@theme/components/NavLinks.vue";
// Import the VersionSwitcher component
import VersionSwitcher from "@theme/components/VersionSwitcher.vue";

export default {
  name: "Navbar",

  components: {
    SidebarButton,
    NavLinks,
    SearchBox,
    AlgoliaSearchBox,
   //VersionSwitcher, // Register the VersionSwitcher component
  },

  data() {
    return {
      linksWrapMaxWidth: null,
      navbarKey: 0, // Key to force re-render
    };
  },

  computed: {
    algolia() {
      return (
        this.$themeLocaleConfig.algolia || this.$site.themeConfig.algolia || {}
      );
    },

    isAlgoliaSearch() {
      return this.algolia && this.algolia.apiKey && this.algolia.indexName;
    },
  },

  methods: {
    homeLink() {
      return this.$store.state.version === "Version 2.x.x"
        ? "/gen2/"
        : "/gen3/";
    },
  },

  mounted() {
    const MOBILE_DESKTOP_BREAKPOINT = 719; // refer to config.styl
    const NAVBAR_VERTICAL_PADDING =
      parseInt(css(this.$el, "paddingLeft")) +
      parseInt(css(this.$el, "paddingRight"));
    const handleLinksWrapWidth = () => {
      if (document.documentElement.clientWidth < MOBILE_DESKTOP_BREAKPOINT) {
        this.linksWrapMaxWidth = null;
      } else {
        this.linksWrapMaxWidth =
          this.$el.offsetWidth -
          NAVBAR_VERTICAL_PADDING -
          ((this.$refs.siteName && this.$refs.siteName.offsetWidth) || 0);
      }
    };
    handleLinksWrapWidth();
    window.addEventListener("resize", handleLinksWrapWidth, false);

    // Listen for nav-updated event to re-render
    this.$router.app.$on("nav-updated", () => {
      this.navbarKey += 1; // Update key to force re-render
    });
  },
};

function css(el, property) {
  // NOTE: Known bug, will return 'auto' if style value is 'auto'
  const win = el.ownerDocument.defaultView;
  // null means not to return pseudo styles
  return win.getComputedStyle(el, null)[property];
}
</script>

<style lang="stylus">
$navbar-vertical-padding = 0.7rem
$navbar-horizontal-padding = 1.5rem

.navbar
  padding $navbar-vertical-padding $navbar-horizontal-padding
  line-height $navbarHeight - 1.4rem
  a, span, img
    display inline-block
  .logo
    height $navbarHeight - 2.3rem
    min-width $navbarHeight - 1.4rem
    margin-right 0.8rem
    vertical-align middle
    margin-top auto
    margin-bottom 0.6rem
  .site-name
    font-size 1.6rem
    font-weight 600
    color $textColor
  .links
    padding-left 1.5rem
    box-sizing border-box
    background-color white
    white-space nowrap
    font-size 0.9rem
    position absolute
    right $navbar-horizontal-padding
    top $navbar-vertical-padding
    display flex
    align-items center
  .search-box
    flex: 0 0 auto
    vertical-align top

@media (max-width: $MQMobile)
  .navbar
    padding-left 4rem
    .can-hide
      display none
    .links
      padding-left 1.5rem
    .site-name
      width calc(100vw - 9.4rem)
      overflow hidden
      white-space nowrap
      text-overflow ellipsis
</style>
