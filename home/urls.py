"""Rutas para home"""
from django.urls import path

from .views import HomeView, curriculums

app_name = "home"

urlpatterns = [
    path('', HomeView.as_view(template_name='home/home.html'), name='home'),
    path('curriculums/', curriculums, name = "listcurriculums")
]