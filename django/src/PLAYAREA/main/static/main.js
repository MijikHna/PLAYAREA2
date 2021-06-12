import Vue from 'vue/dist/vue.js';
import * as $ from 'jquery';

//import vuetify from '@webpack-stuff/vuetify.js';

import Apps from './components/Apps.vue';

$(document).ready(function() {
  if ($('#all-apps').length) {
    new Vue({
      el: '#all-apps',
      render: (h) => h(Apps),
    });
  }
});
