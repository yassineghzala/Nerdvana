from urllib import request, response
from django.shortcuts import render, get_object_or_404 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions 
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response




@api_view(['GET' , 'POST'])
def userGP(request):
    if request.method == 'GET':
        user = User.objects.all(); 
        user_serializer = UserSerializer(user,many=True)
        return JsonResponse(user_serializer.data,safe=False);
    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save();
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET' , 'PUT' , 'DELETE'])
def userGPD(request,pk):
    user = get_object_or_404(User,pk=pk);
    if request.method == 'GET':
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data);
    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(user, data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete();
        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data) 

@api_view(['GET'])
def getUserByEmail(request,email):
    user = get_object_or_404(User,email=email);
    if request.method == 'GET':
        user_serializer = UserSerializer(user)
    return JsonResponse(user_serializer.data,safe=False);



