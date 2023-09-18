from django.shortcuts import render
from rest_framework import viewsets
from .seriealizers import serializermovies,serializerseries
from .models import movies,series

class moviesViewSet(viewsets.ModelViewSet):
    queryset = movies.objects.all()
    serializer_class=serializermovies
    basename='movies'
class seriesViewSet(viewsets.ModelViewSet):
    queryset=series.objects.all()
    serializer_class=serializerseries
    basename='series'
    

# Create your views here.
