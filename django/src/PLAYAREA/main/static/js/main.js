import Vue from 'vue';
import * as $ from 'jquery';

//import vuetify from '@webpack-stuff/vuetify.js';

import TestThreeJs001 from './components/threejs/TestThreeJs001.vue';
import TestThreeJs002 from './components/threejs/TestThreeJs002.vue';
import TestThreeJsCar from './components/threejs/TestThreeJsCar.vue';
import VueTest001 from './components/vuejs/VueTest001/VueTest001.vue';
import VueTest002 from './components/vuejs/VueTest002/VueTest002.vue';
import VueTestModal001 from './components/vuejs/VueTestModal/VueTestModal001.vue';

$(document).ready(function() {
  if ($('#test-threejs-001').length) {
    new Vue({
      el: '#test-threejs-001',
      render: (h) => h(TestThreeJs001),
    });
  }

  if ($('#test-threejs-002').length) {
    new Vue({
      el: '#test-threejs-002',
      render: (h) => h(TestThreeJs002),
    });
  }

  if ($('#test-threejs-car').length) {
    new Vue({
      el: '#test-threejs-car',
      render: (h) => h(TestThreeJsCar),
    });
  }

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
  if ($('#vue-test-modal-001').length) {
    new Vue({
      el: '#vue-test-modal-001',
      render: (h) => h(VueTestModal001),
    });
  }
});
