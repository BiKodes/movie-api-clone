from rest_framework.serializers import ModelSerializer

from .models import Movie, Genre


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name',]

