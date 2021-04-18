import { Vue } from 'vue';
// const Vue = require('vue');
import { MyButton } from './components/MyButton.vue';
// const MyButton = require('./components/MyButton');
import * as $ from 'jquery';

$(document).ready(function() {
  new Vue({
    render: (h) => h(MyButton),
  }).$mount('#my-button');
});
