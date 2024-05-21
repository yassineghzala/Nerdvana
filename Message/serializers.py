from rest_framework import serializers # type: ignore
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message;
        fields = [
            'commandId',
            'content',
            'created_at',
            'sender',
            'receiver',
            ];