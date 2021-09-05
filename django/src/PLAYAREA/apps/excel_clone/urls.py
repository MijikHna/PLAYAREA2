from django.urls import path, re_path

from apps.excel_clone import views

urlpatterns = [
    # HTML
    re_path(r'^(?P<id>[0-9]*)$|^<int:id>$',
            views.open_table, name='open-table'),

    # JSON
    path('new/', views.new_table, name='new-table'),  # redirect
    path('get-tables/', views.get_tables, name='get-tables'),
    path('save/<int:id>/', views.save_table, name='save-table'),
    path('delete/<int:id>/', views.delete_table,
         name='delete-table'),  # redirect
    path('close/<int:id>/', views.close_table, name='close-table')  # redirect
]
