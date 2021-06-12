from django.urls import path, re_path
from django.urls.conf import include

from apps.accounts import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.LoginCustomView.as_view(), name='custom-login'),
    path('logout/', views.LogoutCustomView.as_view(), name='custom-login'),
    path('password_change/', views.PasswordChangeCustomView.as_view(),
         name='custom-password-change'),
    path('password_change/done/', views.PasswordChangeDoneCustomView.as_view(),
         name='password-change-done'),
    path('', include('django.contrib.auth.urls')),
    #path('login/', views.login, name='login'),
    #path('register/', views.register, name='register'),
]

"""
Erstellt:

* accounts/login/ - braucht Template; bei Erfolg Redirect zu /accounts/profile => in settings.py überschreiben
* accounts/logout/ -  braucht kein Template; Bei Erfolg Redirect zu /accounts/logout => in setttings.py überschreiben
* accounts/password_change/ - braucht Template
* accounts/password_change/done/ - braucht Template
* accounts/password_reset/ - braucht Template; wird eMail verwendet
* accounts/password_reset/done/ - braucht Template 
* accounts/reset/<uidb64>/<token>/
* accounts/reset/done/ 
"""
