from django.db import models
from django.contrib.auth.models import User

class Studies(models.Model):
    """modelo para representar estudios"""
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    gradedate = models.DateField()
    school = models.CharField(max_length=50)
    show = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Estudio'
        verbose_name_plural = 'Estudios'

    def __str__(self):
        return self.name
