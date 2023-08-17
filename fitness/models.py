from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    fullname = models.TextField(default=None,blank=True,null=True)
    peso = models.FloatField(default=None,blank=True, max_length=4,null=True)
    altura = models.FloatField(default=None,blank=True,null=True)


    custom_groups = models.ManyToManyField(Group)

class EjerciciosDict(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Lunes = models.JSONField(default=list)   
    Martes = models.JSONField(default=list)
    Miercoles = models.JSONField(default=list)
    Jueves = models.JSONField(default=list)
    Viernes = models.JSONField(default=list)
    Sabado = models.JSONField(default=list)
    Domingo = models.JSONField(default=list)