from django.urls import path

from .views import StudyMain, ExperienceMain, curriculum, studydelete, experiencedelete

app_name="briefcase"

urlpatterns = [
    path('studies/', StudyMain.as_view(), name='studies'),
    path('studies/<int:id>', StudyMain.as_view(), name='study'),
    path('experiences/', ExperienceMain.as_view(), name='experiences'),
    path('experiences/<int:id>', ExperienceMain.as_view(), name='exp'),
    path('curriculum/', curriculum, name='curriculum'),
    path('curriculum/<int:id>', curriculum, name='curriculumparam'),
    path('deletestudy/<int:id>', studydelete, name='deletestudy'),
    path('deleteexperience/<int:id>', experiencedelete, name='deleteexperience'),
]