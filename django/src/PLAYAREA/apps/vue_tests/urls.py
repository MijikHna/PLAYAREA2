from django.urls import path

from apps.vue_tests import views

urlpatterns = [
    path('vue-test-001/', views.vue_test_001, name="vue-test-001"),
    path('vue-test-002/', views.vue_test_002, name="vue-test-002"),
    path('vue-test-003/', views.vue_test_003, name="vue-test-003"),
    path('vue-test-modal-001/', views.vue_test_modal_001,
         name="vue-test-modal-001"),
]
