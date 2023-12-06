from rest_framework import serializers

from films.models import *


class FilmSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    directors = serializers.StringRelatedField(many=True)
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Film
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
