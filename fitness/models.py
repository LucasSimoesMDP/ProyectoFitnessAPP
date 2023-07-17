from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.

class CustomUser(AbstractUser):
    fullname = models.TextField(default=None,blank=True,null=True)
    peso = models.FloatField(default=None,blank=True, max_length=4,null=True)
    altura = models.FloatField(default=None,blank=True,null=True)


    custom_groups = models.ManyToManyField(Group)