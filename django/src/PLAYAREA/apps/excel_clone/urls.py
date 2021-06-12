from django.urls import path

from apps.excel_clone import views

urlpatterns = [
    path('', views.excel_clone, name='excel-clone')
]
