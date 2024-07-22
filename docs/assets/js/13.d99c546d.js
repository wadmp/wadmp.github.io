(window.webpackJsonp=window.webpackJsonp||[]).push([[13],{255:function(t,e,a){},261:function(t,e,a){},262:function(t,e,a){},269:function(t,e,a){},278:function(t,e,a){"use strict";a(255)},285:function(t,e,a){"use strict";a(261)},286:function(t,e,a){"use strict";a(262)},293:function(t,e,a){"use strict";a(269)},589:function(t,e,a){"use strict";var s=a(279),i=a(590),n=a(593),o=a(276),r=a(43),l=a(87),c={computed:{versions:()=>["Version 3.x.x","Version 2.x.x"],currentVersion(){return this.$store.state.version}},methods:{switchVersion(t){const e=t.target.value;switch(this.$store.mutations.setVersion(e),r.a.$emit("version-changed",e),e){case"Version 3.x.x":this.$router.push("/gen3/");break;case"Version 2.x.x":this.$router.push("/gen2/")}this.updateNav(e)},updateNav(t){this.$site.themeConfig.nav=Object(l.getVersionedNav)(t),this.$router.app.$emit("nav-updated")}}},u=(a(285),a(11)),h=Object(u.a)(c,(function(){var t=this,e=t._self._c;return e("div",{staticClass:"version-switcher"},[e("select",{directives:[{name:"model",rawName:"v-model",value:t.$store.state.version,expression:"$store.state.version"}],on:{change:[function(e){var a=Array.prototype.filter.call(e.target.options,(function(t){return t.selected})).map((function(t){return"_value"in t?t._value:t.value}));t.$set(t.$store.state,"version",e.target.multiple?a:a[0])},t.switchVersion]}},t._l(t.versions,(function(a){return e("option",{key:a,domProps:{value:a}},[t._v("\n      "+t._s(a)+"\n    ")])})),0)])}),[],!1,null,null,null).exports;function d(t,e){return t.ownerDocument.defaultView.getComputedStyle(t,null)[e]}var m={name:"Navbar",components:{SidebarButton:n.a,NavLinks:o.a,SearchBox:i.a,AlgoliaSearchBox:s.a,VersionSwitcher:h},data:()=>({linksWrapMaxWidth:null,navbarKey:0}),computed:{algolia(){return this.$themeLocaleConfig.algolia||this.$site.themeConfig.algolia||{}},isAlgoliaSearch(){return this.algolia&&this.algolia.apiKey&&this.algolia.indexName}},methods:{homeLink(){return"Version 2.x.x"===this.$store.state.version?"/gen2/":"/gen3/"}},mounted(){const t=parseInt(d(this.$el,"paddingLeft"))+parseInt(d(this.$el,"paddingRight")),e=()=>{document.documentElement.clientWidth<719?this.linksWrapMaxWidth=null:this.linksWrapMaxWidth=this.$el.offsetWidth-t-(this.$refs.siteName&&this.$refs.siteName.offsetWidth||0)};e(),window.addEventListener("resize",e,!1),this.$router.app.$on("nav-updated",()=>{this.navbarKey+=1})}},p=(a(286),Object(u.a)(m,(function(){var t=this,e=t._self._c;return e("header",{key:t.navbarKey,staticClass:"navbar"},[e("SidebarButton",{on:{"toggle-sidebar":function(e){return t.$emit("toggle-sidebar")}}}),t._v(" "),e("RouterLink",{staticClass:"home-link",attrs:{to:t.homeLink()}},[t.$site.themeConfig.logo?e("img",{staticClass:"logo",attrs:{src:t.$withBase(t.$site.themeConfig.logo),alt:t.$siteTitle}}):t._e(),t._v(" "),t.$siteTitle?e("span",{ref:"siteName",staticClass:"site-name",class:{"can-hide":t.$site.themeConfig.logo}},[t._v("\n      Documentation\n    ")]):t._e()]),t._v(" "),e("div",{staticClass:"links",style:t.linksWrapMaxWidth?{"max-width":t.linksWrapMaxWidth+"px"}:{}},[t.isAlgoliaSearch?e("AlgoliaSearchBox",{attrs:{options:t.algolia}}):!1!==t.$site.themeConfig.search&&!1!==t.$page.frontmatter.search?e("SearchBox"):t._e(),t._v(" "),e("VersionSwitcher"),t._v(" "),e("NavLinks",{staticClass:"can-hide"})],1)],1)}),[],!1,null,null,null));e.a=p.exports},591:function(t,e,a){"use strict";var s={name:"Home",components:{NavLink:a(254).a},computed:{data(){return this.$page.frontmatter},actionLink(){return{link:this.data.actionLink,text:this.data.actionText}},wadmpLink:()=>({link:"https://wadmp.com",text:"wadmp.com"}),apiLink:()=>({link:"https://api.wadmp.com",text:"api.wadmp.com"}),statusLink:()=>({link:"https://status.wadmp.com",text:"status.wadmp.com"})}},i=(a(278),a(11)),n=Object(i.a)(s,(function(){var t=this,e=t._self._c;return e("main",{staticClass:"home",attrs:{"aria-labelledby":null!==t.data.heroText?"main-title":null}},[e("header",{staticClass:"hero"},[t.data.heroImage?e("img",{attrs:{src:t.$withBase(t.data.heroImage),alt:t.data.heroAlt||"hero"}}):t._e(),t._v(" "),null!==t.data.tagline?e("p",{staticClass:"description"},[t._v("\n      "+t._s(t.data.tagline||t.$description||"Welcome to your VuePress site")+"\n    ")]):t._e()]),t._v(" "),e("Content",{staticClass:"theme-default-content custom"}),t._v(" "),t.data.features&&t.data.features.length?e("div",{staticClass:"features"},t._l(t.data.features,(function(a,s){return e("div",{key:s,staticClass:"feature"},[e("h2",[t._v(t._s(a.title))]),t._v(" "),e("p",[t._v(t._s(a.details))])])})),0):t._e(),t._v(" "),t.data.footer?e("div",{staticClass:"footer"},[t._v("\n    "+t._s(t.data.footer)+"\n  ")]):e("Content",{staticClass:"footer",attrs:{"slot-key":"footer"}})],1)}),[],!1,null,null,null);e.a=n.exports},592:function(t,e,a){"use strict";var s=a(275),i=a(276),n={name:"Sidebar",components:{SidebarLinks:s.default,NavLinks:i.a},props:["items"],data:()=>({sidebarKey:0}),mounted(){this.$router.app.$on("nav-updated",()=>{this.sidebarKey+=1})}},o=(a(293),a(11)),r=Object(o.a)(n,(function(){var t=this._self._c;return t("aside",{key:this.sidebarKey,staticClass:"sidebar"},[t("NavLinks"),this._v(" "),this._t("top"),this._v(" "),t("SidebarLinks",{attrs:{depth:0,items:this.items}}),this._v(" "),this._t("bottom")],2)}),[],!1,null,null,null);e.a=r.exports}}]);