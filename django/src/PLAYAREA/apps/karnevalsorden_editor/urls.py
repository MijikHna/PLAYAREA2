from django.urls import path

from apps.karnevalsorden_editor import views

urlpatterns = [
    path('', views.index, name='karnevalsorden-editor'),
]
