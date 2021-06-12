const entries = {
  // everywhere = in BASE.html
  'playarea-base': './static/main.js',
  'main': './main/static/main.js',
  'header': './static/js/header.js',
  //accounts
  'apps/accounts': './apps/accounts/static/main.js',
  'apps/accounts/dashboard': './apps/accounts/static/js/dashboard.js',
  //karnevalsorde_editor
  'apps/karnevalsorden_editor':
    './apps/karnevalsorden_editor/static/js/main.js',
  // threejs-tests
  'apps/threejs_tests': './apps/threejs_tests/static/main.js',
  // vue -tests
  'apps/vue_tests': './apps/vue_tests/static/main.js',
  // various
  'apps/various': './apps/various/static/main.js',
  'apps/various/pure-js-component-main':
    './apps/various/static/js/pure-js-component-main.js',
};

module.exports = entries;
