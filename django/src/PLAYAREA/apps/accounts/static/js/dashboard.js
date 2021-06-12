import Vue from 'vue';
import '../css/sidebar.scss';

import NavLinkButton from '../components/NavLinkButton';
import NotifierRoot from '@app/static/components/NotifierRoot';

$(document).ready(function() {
  $('#sidebarCollapse').on('click', () => {
    toggleSideBar();
  });
  $('#sidebarCollapseNav').on('click', () => {
    toggleSideBar();
  });

  const navLinkButtons = $('ul#sidebar-nav').children();
  for (const navLinkButton of navLinkButtons) {
    new Vue({
      el: navLinkButton,
      render: (h) => h(NavLinkButton),
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

function toggleSideBar() {
  $('#sidebar').toggleClass('active');
  $('#sidebarCollapse').toggleClass('d-none');
  $('#content nav').toggleClass('justify-content-between');
  $('#content nav').toggleClass('justify-content-end');
}
