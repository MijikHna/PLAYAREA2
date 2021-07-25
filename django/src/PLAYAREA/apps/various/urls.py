from django.urls import path

from apps.various import views

urlpatterns = [
    path('pure-js-component/', views.pure_js_component, name='pure-js-component'),
    path('daterangepicker/', views.daterangepicker, name='daterangepicker'),
    path('custom-html/', views.custom_html, name='custom-html'),
    # rpc tests
    path('test-rpc-1/', views.test_rpc_1, name='test-rpc-1'),
    path('test-rpc-1/all/', views.test_rpc_1_all, name='test-rpc-1-all'),
    path('test-rpc-1/<int:id>/', views.test_rpc_1_with_id,
         name='test-rpc-1-with-id'),
    path('test-rpc-1/create/', views.test_rpc_1_create, name='test-rpc-1-create'),
    path('css-swipe-animation/', views.css_swipe_animation, name='css-swipe-animation'),
]
