(window.webpackJsonp=window.webpackJsonp||[]).push([[12],{237:function(t,a,e){},243:function(t,a,e){},258:function(t,a,e){"use strict";e(237)},265:function(t,a,e){"use strict";e(243)},420:function(t,a,e){"use strict";var i={name:"Home",components:{NavLink:e(236).a},computed:{data(){return this.$page.frontmatter},actionLink(){return{link:this.data.actionLink,text:this.data.actionText}},wadmpLink:()=>({link:"https://wadmp.com",text:"wadmp.com"}),apiLink:()=>({link:"https://api.wadmp.com",text:"api.wadmp.com"}),statusLink:()=>({link:"https://status.wadmp.com",text:"status.wadmp.com"})}},s=(e(258),e(10)),n=Object(s.a)(i,(function(){var t=this,a=t._self._c;return a("main",{staticClass:"home",attrs:{"aria-labelledby":null!==t.data.heroText?"main-title":null}},[a("header",{staticClass:"hero"},[t.data.heroImage?a("img",{attrs:{src:t.$withBase(t.data.heroImage),alt:t.data.heroAlt||"hero"}}):t._e(),t._v(" "),null!==t.data.tagline?a("p",{staticClass:"description"},[t._v("\n      "+t._s(t.data.tagline||t.$description||"Welcome to your VuePress site")+"\n    ")]):t._e()]),t._v(" "),a("Content",{staticClass:"theme-default-content custom"}),t._v(" "),t.data.features&&t.data.features.length?a("div",{staticClass:"features"},t._l(t.data.features,(function(e,i){return a("div",{key:i,staticClass:"feature"},[a("h2",[t._v(t._s(e.title))]),t._v(" "),a("p",[t._v(t._s(e.details))])])})),0):t._e(),t._v(" "),t.data.footer?a("div",{staticClass:"footer"},[t._v("\n    "+t._s(t.data.footer)+"\n  ")]):a("Content",{staticClass:"footer",attrs:{"slot-key":"footer"}})],1)}),[],!1,null,null,null);a.a=n.exports},421:function(t,a,e){"use strict";var i=e(259),s=e(419),n=e(422),o=e(256);function l(t,a){return t.ownerDocument.defaultView.getComputedStyle(t,null)[a]}var r={name:"Navbar",components:{SidebarButton:n.a,NavLinks:o.a,SearchBox:s.a,AlgoliaSearchBox:i.a},data:()=>({linksWrapMaxWidth:null}),computed:{algolia(){return this.$themeLocaleConfig.algolia||this.$site.themeConfig.algolia||{}},isAlgoliaSearch(){return this.algolia&&this.algolia.apiKey&&this.algolia.indexName}},mounted(){const t=parseInt(l(this.$el,"paddingLeft"))+parseInt(l(this.$el,"paddingRight")),a=()=>{document.documentElement.clientWidth<719?this.linksWrapMaxWidth=null:this.linksWrapMaxWidth=this.$el.offsetWidth-t-(this.$refs.siteName&&this.$refs.siteName.offsetWidth||0)};a(),window.addEventListener("resize",a,!1)}},c=(e(265),e(10)),d=Object(c.a)(r,(function(){var t=this,a=t._self._c;return a("header",{staticClass:"navbar"},[a("SidebarButton",{on:{"toggle-sidebar":function(a){return t.$emit("toggle-sidebar")}}}),t._v(" "),a("RouterLink",{staticClass:"home-link",attrs:{to:t.$localePath}},[t.$site.themeConfig.logo?a("img",{staticClass:"logo",attrs:{src:t.$withBase(t.$site.themeConfig.logo),alt:t.$siteTitle}}):t._e(),t._v(" "),t.$siteTitle?a("span",{ref:"siteName",staticClass:"site-name",class:{"can-hide":t.$site.themeConfig.logo}},[t._v("Documentation")]):t._e()]),t._v(" "),a("div",{staticClass:"links",style:t.linksWrapMaxWidth?{"max-width":t.linksWrapMaxWidth+"px"}:{}},[t.isAlgoliaSearch?a("AlgoliaSearchBox",{attrs:{options:t.algolia}}):!1!==t.$site.themeConfig.search&&!1!==t.$page.frontmatter.search?a("SearchBox"):t._e(),t._v(" "),a("NavLinks",{staticClass:"can-hide"})],1)],1)}),[],!1,null,null,null);a.a=d.exports}}]);