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

  // assign js variable "table" provided by django rendering to vue store and delete this js variable
  if (window?.table) {
    excelClone.$store.commit('setTable', window.table);
    delete window.table;
    window['table'] = undefined;
  }
});
