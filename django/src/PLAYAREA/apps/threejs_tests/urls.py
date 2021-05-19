from django.urls import path

from apps.threejs_tests import views

urlpatterns = [
    path('test-threejs-001/', views.test_threejs_001, name='test-threejs-001'),
    path('test-threejs-002/', views.test_threejs_002, name='test-threejs-002'),
    path('test-threejs-car/', views.test_threejs_car, name='test-threejs-car'),
]
