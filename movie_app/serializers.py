from .models import Movie, Review, Director
from rest_framework import serializers


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = [
            "name",
        ]


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            "title",
            "description",
            "duration",
            "director",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "text",
            "movie",
        ]
