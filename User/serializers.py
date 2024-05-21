from rest_framework import serializers # type: ignore
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User;
        fields = [
            'userId',
            'username',
            'password',
            'email',
            'isAdmin'
            ];