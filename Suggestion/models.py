from django.db import models

# Create your models here.
class Suggestion(models.Model):
    suggestionID = models.AutoField(primary_key=True);
    content = models.CharField();
    pass