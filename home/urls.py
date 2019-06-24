from django.urls import path

from .views import HomeView

app_name="home"

urlpatterns = [
    path('', HomeView.as_view(template_name='home/home.html'), name='home'),
]