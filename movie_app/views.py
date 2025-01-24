from django.shortcuts import render
from rest_framework import generics
from .models import Director, Movie, Review
from .serializers import MovieSerializer, ReviewSerializer, DirectorSerializer


class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    loockup_field = "id"


class DirectroDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    loockup_field = "id"


class MovieDetailAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    loockup_field = "id"


class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    loockup_field = "id"


class RewiewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class RewiewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    loockup_field = "id"
