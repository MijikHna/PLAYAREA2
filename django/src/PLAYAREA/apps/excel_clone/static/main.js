import Vue from 'vue';
import * as $ from 'jquery';

import vuetify from '@webpack-stuff/vuetify.js';

import ExcelClone from './components/ExcelClone.vue';
import excelCloneStore from './js/excelClone-store.js';

$(() => {
  if ($('#excel-clone').length) {
    globalThis.excelClone = new Vue({
      vuetify,
      el: '#excel-clone',
      store: excelCloneStore,
      components: { ExcelClone },
      render: (h) => h(ExcelClone),
    });
  }
});
