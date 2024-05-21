from django.db import models

from User.models import User

# Create your models here.
class Message(models.Model):
    messsageId = models.AutoField(primary_key=True);
    content = models.CharField(max_length=25);
    created_at = models.DateTimeField();
    sender = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='messages_sent');
    receiver = models.ForeignKey(User, on_delete=models.CASCADE,null=True, related_name='messages_received');
