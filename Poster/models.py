from django.db import models

# Create your models here.
class Poster(models.Model):
    posterId = models.AutoField(primary_key=True);
    quantity = models.PositiveIntegerField();
    artist = models.CharField(max_length=25);
    album = models.CharField(max_length=25);
    added_at = models.DateTimeField(null=True);
    updated_at = models.DateTimeField(null=True);
    posterFile = models.FileField(null=True);
def __init__(self, quantity, artist, album,added_at,updated_at,imageURL):
        self.quantity = quantity;
        self.artist = artist; 
        self.album = album; 
        self.added_at = added_at; 
        self.updated_at = updated_at;
        self.imageURL = imageURL; 