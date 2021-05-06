import Vue from 'vue';
import * as $ from 'jquery';

import vuetify from '@webpack-stuff/vuetify.js';

import MyButton from './components/MyButton.vue';

$(document).ready(function() {
  new Vue({
    vuetify,
    render: (h) => h(MyButton),
  }).$mount('#my-button');
});
