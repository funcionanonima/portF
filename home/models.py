"""Modelos de home"""
from django.db import models

# Create your models here.

class Message(models.Model):
    """modelo para representar mensajes de contacto"""
    id = models.AutoField('id', primary_key=True)
    email = models.EmailField('email')
    name = models.CharField(max_length=50)
    body = models.TextField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Mensaje"
        verbose_name_plural = 'Mensajes'
        