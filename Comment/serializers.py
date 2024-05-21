from rest_framework import serializers # type: ignore
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment;
        fields = [
            'id',
            'content',
            'postId',
            'userId'
            ];