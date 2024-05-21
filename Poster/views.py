from django.shortcuts import render,  get_object_or_404 
from rest_framework.decorators import api_view
from Poster.models import Poster
from Poster.serializers import PosterSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status


from django.core.files.storage import default_storage
from django.contrib import messages

from django.shortcuts import render, redirect
from django.shortcuts import render





# Create your views here.
@api_view(['GET' , 'POST'])
def posterGP(request):
    body = request.body;
    if request.method == 'GET':
        posters = Poster.objects.all();
        poster_serializer = PosterSerializer(posters, many=True);
        return JsonResponse(poster_serializer.data,safe=False);
    elif request.method == 'POST':
        poster_data = JSONParser().parse(request)
        poster_serializer = PosterSerializer(data=poster_data)
        if poster_serializer.is_valid():
            poster_serializer.save();
            return JsonResponse(poster_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(poster_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET' , 'PUT' , 'DELETE'])
def posterGPD(request,pk):
    poster = get_object_or_404(Poster,pk=pk);
    if request.method == 'GET':
        poster_serializer = PosterSerializer(poster)
        return JsonResponse(poster_serializer.data);
    elif request.method == 'PUT':
        poster_data = JSONParser().parse(request)
        poster_serializer = PosterSerializer(poster, data=poster_data)
        if poster_serializer.is_valid():
            poster_serializer.save()
            return JsonResponse(poster_serializer.data) 
        return JsonResponse(poster_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        poster.delete();


#@api_view(['GET'])
#def postersByAlbum(request,album):
#    posters = Poster.objects.all();
#    filteredPosters = posters.filter(album=album);
#    if request.method == 'GET':
#        poster_serializer = PosterSerializer(filteredPosters);
#        return JsonResponse(poster_serializer.data);
#
#@api_view(['GET'])
#def postersByArtist(request,artist):
#    posters = Poster.objects.all();
#    filteredPosters = posters.filter(artist=artist);
#    if request.method == 'GET':
#        poster_serializer = PosterSerializer(filteredPosters);
#        return JsonResponse(poster_serializer.data);

from rest_framework import generics

class PostersByArtistView(generics.ListAPIView):
    serializer_class = PosterSerializer

    def get_queryset(self):
        artist = self.kwargs['artist']
        return Poster.objects.filter(artist=artist)
    
class PostersByAlbumView(generics.ListAPIView):
    serializer_class = PosterSerializer

    def get_queryset(self):
        album = self.kwargs['album']
        return Poster.objects.filter(album=album)











