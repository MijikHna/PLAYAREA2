import Vue from 'vue';
import MyButton from './components/MyButton.vue';
import * as $ from 'jquery';

$(document).ready(function() {
  new Vue({
    render: (h) => h(MyButton),
  }).$mount('#my-button');
});
