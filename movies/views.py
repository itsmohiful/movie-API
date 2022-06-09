from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.serializers import Serializer
from .serializers import MovieSerializer
from .models import MovieData


class MovieViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category='action')
    serializer_class = MovieSerializer


class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category='comedy')
    serializer_class = MovieSerializer


class ArtisticViewset(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category='artistic')
    serializer_class = MovieSerializer
