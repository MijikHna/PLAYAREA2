import Vue from 'vue';
import * as $ from 'jquery';

import CarMenu from './components/CarMenu.vue';

$(document).ready(function() {
  if ($('#test-rpc-1').length) {
    new Vue({
      el: '#test-rpc-1',
      components: { CarMenu },
      render: (h) => h(CarMenu),
    });
  }
});
