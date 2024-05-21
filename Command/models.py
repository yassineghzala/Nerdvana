from django.db import models

from Poster.models import Poster

from User.models import User
# Create your models here.
class Command(models.Model):
    
    id = models.AutoField(primary_key=True);
    posters = models.ManyToManyField(Poster);
    userId = models.ForeignKey(User, on_delete=models.CASCADE,null=True);
    location = models.CharField(max_length=25,null=True)

