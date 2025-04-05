from django.contrib.auth import views as auth_views
from django.urls import path

from .views import dashboard

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-change/', auth_views.PasswordChangeView.as_view(), name='Password_Change'),
    path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('passord-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('passord-reset-done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('', dashboard, name='dashboard'),
]
