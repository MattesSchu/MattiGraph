(window.webpackJsonp=window.webpackJsonp||[]).push([[7],{177:function(e,n,a){"use strict";a(24),a(20),a(76),a(52),a(19);var r=a(0),c=a.n(r),t=a(174),s=a.n(t),o=a(172),i=a(168);n.a=function(e){var n=Object(r.useRef)(!1),t=Object(r.useRef)(null),u=Object(o.b)(),l=Object(i.a)().siteConfig,h=(void 0===l?{}:l).baseUrl,d=function(){n.current||(Promise.all([fetch(h+"search-doc.json").then((function(e){return e.json()})),fetch(h+"lunr-index.json").then((function(e){return e.json()})),Promise.all([a.e(31),a.e(34)]).then(a.bind(null,182)),a.e(25).then(a.t.bind(null,181,7))]).then((function(e){!function(e,n,a){new a({searchDocs:e,searchIndex:n,inputSelector:"#search_input_react",handleSelected:function(e,n,a){var r=h+a.url;document.createElement("a").href=r,u.push(r)}})}(e[0],e[1],e[2].default)})),n.current=!0)},b=Object(r.useCallback)((function(n){t.current.contains(n.target)||t.current.focus(),e.handleSearchBarToggle(!e.isSearchBarExpanded)}),[e.isSearchBarExpanded]);return c.a.createElement("div",{className:"navbar__search",key:"search-box"},c.a.createElement("span",{"aria-label":"expand searchbar",role:"button",className:s()("search-icon",{"search-icon-hidden":e.isSearchBarExpanded}),onClick:b,onKeyDown:b,tabIndex:0}),c.a.createElement("input",{id:"search_input_react",type:"search",placeholder:"Search","aria-label":"Search",className:s()("navbar__search-input",{"search-bar-expanded":e.isSearchBarExpanded},{"search-bar":!e.isSearchBarExpanded}),onClick:d,onMouseOver:d,onFocus:b,onBlur:b,ref:t}))}}}]);