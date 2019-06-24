from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from .views import Register, Profile, Edit, ChangePassword, Info

# rutas para accounts

app_name="accounts"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', Register, name='register'),
    path('profile/', Profile, name='profile'),
    path('edit/', Edit, name='edit'),
    path('info', Info, name='info'),
    path('changepassword/', ChangePassword, name='changepassword'),    
    # path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    # path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'), 
    # path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'), 
    # path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]