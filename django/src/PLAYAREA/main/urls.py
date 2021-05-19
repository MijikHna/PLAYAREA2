from django.urls import path

from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get-all-apps/', views.getAllApps, name='get-all-apps')
]
