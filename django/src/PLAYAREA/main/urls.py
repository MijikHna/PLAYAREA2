from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    # threejs
    path('main/threesjs/test-threejs-001/',
         views.test_threejs_001, name='test-threejs-001'),
    path('main/threejs/test-threejs-002/',
         views.test_threejs_002, name='test-threejs-002'),
    path('main/threejs/test-threejs-car/',
         views.test_threejs_car, name='test-threejs-car'),
    # vue
    path('main/vue/vue-test-001', views.vue_test_001, name="vue-test-001"),
    path('main/vue/vue-test-002', views.vue_test_002, name="vue-test-002"),
    path('main/vue/vue-test-modal-001', views.vue_test_modal_001,
         name="vue-test-modal-001"),
    # various
    path('main/various/pure-js-component', views.pure_js_component,
         name='pure-js-component'),
]
