import Vue from 'vue';
import * as $ from 'jquery';

import HeaderVue from '@app/static/components/HeaderApp.vue';
import HeaderMainApp from '@app/static/components/HeaderMainApp.vue';

$(document).ready(function() {
  let navApps = $("a[data-type='nav-app']");

  if (navApps.length) {
    for (const navApp of navApps) {
      new Vue({
        el: navApp,
        render: (h) => h(HeaderVue),
      });
    }
  }

  navApps = $("a[data-type='nav-mainapp']");

  if (navApps.length) {
    for (const navApp of navApps) {
      new Vue({
        el: navApp,
        render: (h) => h(HeaderMainApp),
      });
    }
  }
});
