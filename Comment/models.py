from django.db import models

from Post.models import Post
from User.models import User

# Create your models here.
class Comment(models.Model):
    id = models.AutoField(primary_key=True);
    content = models.CharField(max_length=25)
    postId = models.ForeignKey(Post, on_delete=models.CASCADE,null=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE,null=True)