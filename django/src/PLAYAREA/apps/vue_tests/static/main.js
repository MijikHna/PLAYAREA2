import Vue from 'vue';
import * as $ from 'jquery';

import VueTest001 from './components/VueTest001/VueTest001.vue';
import VueTest002 from './components/VueTest002/VueTest002.vue';
import VueTest003 from './components/VueTest003/VueTest003.vue';
import VueTestModal001 from './components/VueTestModal/VueTestModal001.vue';

$(document).ready(function() {
  if ($('#vue-test-001').length) {
    new Vue({
      el: '#vue-test-001',
      render: (h) => h(VueTest001),
    });
  }

  if ($('#vue-test-002').length) {
    new Vue({
      el: '#vue-test-002',
      render: (h) => h(VueTest002),
    });
  }
  if ($('#vue-test-003').length) {
    new Vue({
      el: '#vue-test-003',
      render: (h) => h(VueTest003),
    });
  }
  if ($('#vue-test-modal-001').length) {
    new Vue({
      el: '#vue-test-modal-001',
      render: (h) => h(VueTestModal001),
    });
  }
});
