from django.db import models

from Poster.models import Poster # type: ignore

# Create your models here.
class User(models.Model):
    userId = models.AutoField(primary_key=True);
    username = models.CharField(max_length=25);
    password = models.CharField(max_length=25);
    email = models.CharField(max_length=25);
    numero = models.IntegerField(null=True);
    isAdmin = models.BooleanField();