from django.shortcuts import render
from django.http import JsonResponse
from Command.models import Command
from Command.serializers import CommandSerializer
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import render,  get_object_or_404 


# Create your views here.
@api_view(['GET' , 'POST'])
def commandsGP(request):
    body = request.body;
    if request.method == 'GET':
        commands = Command.objects.all();
        command_serializer = CommandSerializer(commands, many=True);
        return JsonResponse(command_serializer.data,safe=False);
    elif request.method == 'POST':
        command_data = JSONParser().parse(request)
        command_serializer = CommandSerializer(data=command_data);
        if command_serializer.is_valid():
            command_serializer.save();
            return JsonResponse(command_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(command_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET' , 'PUT' , 'DELETE'])
def commandsGPD(request,pk):
    command = get_object_or_404(Command,pk=pk);
    if request.method == 'GET':
        command_serializer = CommandSerializer(command);
        return JsonResponse(command_serializer.data);
    elif request.method == 'PUT':
        command_data = JSONParser().parse(request);
        command_serializer = CommandSerializer(post, data=command_data)
        if command_serializer.is_valid():
            command_serializer.save();
            return JsonResponse(command_serializer.data);
        return JsonResponse(command_serializer.errors, status=status.HTTP_400_BAD_request)
    elif request.method == 'DELETE':
        command.delete();