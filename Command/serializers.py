from Command.models import Command

from Poster.models import Poster
from Poster.serializers import PosterSerializer
from User.models import User
from User.serializers import UserSerializer
from rest_framework import serializers 


class CommandSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = Command;
        fields = [
            'id',
            'posters',
            'userId'
            ];
    


    #def create(self, validated_data):
    #    user_data = validated_data.pop('user');
    #    poster_data = validated_data.pop('poster');
    #    poster, created = Poster.objects.get_or_create(**poster_data);  # Pop user data from validated_data
    #    user, created = User.objects.get_or_create(**user_data);  # Get or create User instance
    #    command = Command.objects.create(user=user,poster=poster, **validated_data);  # Create Poster instance
    #    return command