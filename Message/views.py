from urllib import request, response
from django.shortcuts import render, get_object_or_404 
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import generics, permissions 
from .models import Message
from .serializers import MessageSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response




@api_view(['GET' , 'POST'])
def messageGP(request):
    if request.method == 'GET':
        message = Message.objects.all(); 
        message_serializer = MessageSerializer(message,many=True)
        return JsonResponse(message_serializer.data,safe=False);
    elif request.method == 'POST':
        message_data = JSONParser().parse(request)
        message_serializer = MessageSerializer(data=message_data)
        if message_serializer.is_valid():
            message_serializer.save();
            return JsonResponse(message_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET' , 'PUT' , 'DELETE'])
def messageGPD(request,pk):
    message = get_object_or_404(Message,pk=pk);
    if request.method == 'GET':
        message_serializer = MessageSerializer(message)
        return JsonResponse(message_serializer.data);
    elif request.method == 'PUT':
        message_data = JSONParser().parse(request)
        message_serializer = MessageSerializer(message, data=message_data)
        if message_serializer.is_valid():
            message_serializer.save()
            return JsonResponse(message_serializer.data) 
        return JsonResponse(message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        message.delete();
        message_serializer = MessageSerializer(message)
        return JsonResponse(message_serializer.data) 




