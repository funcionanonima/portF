"""Urls accounts"""
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from .views import register, profile, edit, changepassword, info

# rutas para accounts

app_name = "accounts"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('edit/', edit, name='edit'),
    path('info', info, name='info'),
    path('changepassword/', changepassword, name='changepassword'),    
    # path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    # path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'), 
    # path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
    # path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]