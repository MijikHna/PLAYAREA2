import Vue from 'vue';
import * as $ from 'jquery';

//import vuetify from '@webpack-stuff/vuetify.js';

import TestThreeJs001 from './components/TestThreeJs001.vue';
import TestThreeJs002 from './components/TestThreeJs002.vue';
import TestThreeJsCar from './components/TestThreeJsCar.vue';

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
});
