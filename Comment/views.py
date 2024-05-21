from urllib import request, response
from django.shortcuts import render, get_object_or_404 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions 
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response




@api_view(['GET' , 'POST'])
def commentGP(request):
    if request.method == 'GET':
        comment = Comment.objects.all(); 
        comment_serializer = CommentSerializer(comment,many=True)
        return JsonResponse(comment_serializer.data,safe=False);
    elif request.method == 'POST':
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentSerializer(data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save();
            return JsonResponse(comment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET' , 'PUT' , 'DELETE'])
def commentGPD(request,pk):
    comment = get_object_or_404(Comment,pk=pk);
    if request.method == 'GET':
        comment_serializer = CommentSerializer(comment)
        return JsonResponse(comment_serializer.data);
    elif request.method == 'PUT':
        comment_data = JSONParser().parse(request)
        comment_serializer = CommentSerializer(comment, data=comment_data)
        if comment_serializer.is_valid():
            comment_serializer.save()
            return JsonResponse(comment_serializer.data) 
        return JsonResponse(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        comment.delete();
        comment_serializer = CommentSerializer(comment)
        return JsonResponse(comment_serializer.data) 



