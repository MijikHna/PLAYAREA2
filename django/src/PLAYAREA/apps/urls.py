from django.urls import path, include

urlpatterns = [
    path('accounts/', include('apps.accounts.urls')),
    path('karnevalsorden-editor/', include('apps.karnevalsorden_editor.urls')),
    path('threejs_tests/', include('apps.threejs_tests.urls')),
    path('various/', include('apps.various.urls')),
    path('vue_tests/', include('apps.vue_tests.urls')),
    path('excel-clone/', include('apps.excel_clone.urls')),
]
