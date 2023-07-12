from django.db import models
from django.contrib.auth.models import AbstractUser, Group

# Create your models here.

class CustomUser(AbstractUser):
    fullname = models.TextField(blank=True)
    peso = models.FloatField(blank=True)
    altura = models.FloatField(blank=True)

    custom_groups = models.ManyToManyField(Group)

    def __str__(self):
        return self.username