from User.serializers import UserSerializer
from rest_framework import serializers # type: ignore
from Post.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post;
        fields = [
            'id',
            'imageURL',
            'description',
            'userId',
            'likes'
            ];