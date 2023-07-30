from django.shortcuts import render

from rest_framework import generics
from .models import Place
from .serializers import PlaceSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

class PlaceListCreateAPIView(generics.ListCreateAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class PlaceDeleteAPIView(generics.DestroyAPIView):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer



@api_view(['GET'])
def place_search(request):
    query = request.GET.get('query', '')

    if query:
        places = Place.objects.filter(
            name__icontains=query) | Place.objects.filter(description__icontains=query)
        serializer = PlaceSerializer(places, many=True)
        return Response(serializer.data)
    else:
        return Response([])
    
def place_list(request):
    return render(request, 'place_list.html')