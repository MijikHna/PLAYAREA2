from django.urls import path

from KARNEVALSORDEN_EDITOR import views

urlpatterns = [
    path('', views.index, name='index'),
]
