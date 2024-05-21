from rest_framework import serializers # type: ignore
from Poster.models import Poster

class PosterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Poster;
        fields = [
            'posterId',
            'quantity',
            'artist',
            'album',
            'added_at',
            'updated_at',
            'posterFile'
            ];