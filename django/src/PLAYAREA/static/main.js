// import Vue from 'vue/dist/vue.js';
import Vue from 'vue';
import * as $ from 'jquery';

import NotifierRoot from './components/NotifierRoot';

$(document).ready(function() {
  if ($('#notifier-root').length) {
    globalThis.notifier = new Vue({
      el: '#notifier-root',
      render: (h) => h(NotifierRoot),
    });
  }
});
