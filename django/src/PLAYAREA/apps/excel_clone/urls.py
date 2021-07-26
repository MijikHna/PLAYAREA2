from django.urls import path

from apps.excel_clone import views

urlpatterns = [
    path('', views.excel_clone, name='excel-clone'),
    path('new/', views.new_table, name='new-table'),
    path('get-tables/', views.get_tables, name='get-tables'),
    path('open/<int:id>/', views.open_table, name='open-table'),
    path('save/<int:id>/', views.save_table, name='save-table'),
    path('delete/<int:id>/', views.delete_table, name='delete-table'),
    path('close/<int:id>/', views.close_table, name='close-table')
]
