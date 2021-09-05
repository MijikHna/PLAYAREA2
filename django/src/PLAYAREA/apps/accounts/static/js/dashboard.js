import Vue from 'vue';
import '../css/sidebar.scss';

import SideNav from '../components/SideNav.vue';
import NotifierRoot from '@app/static/components/NotifierRoot';

// $(document).ready(function() {
$(() => {
  $('#sidebarCollapse').on('click', () => {
    toggleSideBar();
  });
  $('#sidebarCollapseNav').on('click', () => {
    toggleSideBar();
  });

  if ($('#vue-side-navigation').length) {
    new Vue({
      el: '#vue-side-navigation',
      render: (h) => h(SideNav),
    });
  }

  $(`#${pictureFileInputId}`).on('change', function() {
    //get the file name
    var fileName = $(this)
      .val()
      .replace(/^.*\\/, '');
    //replace the "Choose a file" label
    $(this)
      .next('.custom-file-label')
      .html(fileName);
  });

  if ($('#notifier-root').length) {
    globalThis.notifier = new Vue({
      el: '#notifier-root',
      render: (h) => h(NotifierRoot),
    });
  }

  if (notifier !== undefined && $('#notifier-data').length) {
    let notifierDataElem = $('#notifier-data')[0];
    notifier.$children[0].$refs.notifierWrapper.addNotifier(
      notifierDataElem.dataset.notifierName,
      notifierDataElem.dataset.notifierMessage,
      notifierDataElem.dataset.result
    );
  }
});

window.toggleSideBar = () => {
  $('#sidebar').toggleClass('active');
  $('#sidebarCollapse').toggleClass('d-none');
  $('#content nav').toggleClass('justify-content-between');
  $('#content nav').toggleClass('justify-content-end');
};
