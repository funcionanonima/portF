from django.db import models
# signal para crear perfil de usuario una vez creao el usuario
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    documenttype = models.CharField(max_length=50)
    document = models.CharField(max_length=50) 
    civilstatus = models.CharField(max_length=50) 
    ethnicgroup = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars', blank=True)

    class Meta:
        verbose_name='Perfil usuario'
        verbose_name_plural='Perfiles de usuario'

    def __str__(self):
        return self.user.username  

def create_profile(sender, **kwargs):
    #si el usuario es creado..
    if kwargs['created']:
        #crea instancia de perfildeusuario
        UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)