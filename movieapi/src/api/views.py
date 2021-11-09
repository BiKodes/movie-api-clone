from django.shortcuts import render

from rest_framework.generics import (ListAPIView, 
                                    CreateAPIView, 
                                    RetrieveAPIView, 
                                    ListCreateAPIView
)
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from api.models import Movie, Genre
from api.serializers import MovieSerializer, GenreSerializer


class MovieListView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'genre__name', 'language', 'type']

class MovieCreateView(CreateAPIView):
    serializer_class = MovieSerializer

class MovieDetailView(RetrieveAPIView):
    queryset = Movie.objects.all()
    lookup_field = 'title'
    serializer_class = MovieSerializer

class GenreCreateListView(ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name',]




