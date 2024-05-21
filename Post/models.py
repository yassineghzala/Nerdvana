from django.db import models

from User.models import User
from User.serializers import UserSerializer
from User.views import userGPD
from django.shortcuts import render,  get_object_or_404 


# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True);
    imageURL = models.CharField(max_length=25,null=False);
    description = models.CharField(max_length=25);
    userId = models.ForeignKey(User, on_delete=models.CASCADE);
    likes = models.IntegerField(null=True);
    