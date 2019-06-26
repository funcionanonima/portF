"""portF URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

#para trabajar con media
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from .views import login_redirect

urlpatterns = [
    path('', login_redirect, name='login_redirect'),
    path('admin/', admin.site.urls),
    #se agregan urls de
    path('account/', include('accounts.urls', namespace='accounts')),
    path('home/', include('home.urls', namespace='home')),
    path('briefcase/', include('briefcase.urls', namespace='briefcase')), 
    # path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    # path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset-password/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
