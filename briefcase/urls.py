from django.urls import path

from .views import StudyMain, ExperienceMain

app_name="briefcase"

urlpatterns = [
    path('studies/', StudyMain.as_view(), name='studies'),
    path('studies/<int:id>', StudyMain.as_view(), name='study'),
    path('experiences/', ExperienceMain.as_view(), name='experiences'),
    path('experiences/<int:id>', ExperienceMain.as_view(), name='exp'),
]