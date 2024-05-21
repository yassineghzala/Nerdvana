from django.shortcuts import render
from django.http import JsonResponse
from Post.models import Post
from Post.serializers import PostSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render,  get_object_or_404 


# Create your views here.
@api_view(['GET' , 'POST'])
def postGP(request):
    body = request.body;
    if request.method == 'GET':
        posts = Post.objects.all();
        post_serializer = PostSerializer(posts, many=True);
        return JsonResponse(post_serializer.data,safe=False);
    elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data);
        if post_serializer.is_valid():
            post_serializer.save();
            return JsonResponse(post_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET' , 'PUT' , 'DELETE'])
def postGPD(request,pk):
    post = get_object_or_404(Post,pk=pk);
    if request.method == 'GET':
        post_serializer = PostSerializer(post);
        return JsonResponse(post_serializer.data);
    elif request.method == 'PUT':
        post_data = JSONParser().parse(request);
        post_serializer = PostSerializer(post, data=post_data)
        if post_serializer.is_valid():
            post_serializer.save();
            return JsonResponse(post_serializer.data);
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_request)
    elif request.method == 'DELETE':
        post.delete();