from django.urls import path

from .views import StudyMain

app_name="briefcase"

urlpatterns = [
    path('studies/', StudyMain.as_view(), name='studies'),
    path('studies/<int:id>/', StudyMain.as_view(), name='study'),
]