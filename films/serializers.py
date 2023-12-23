from django.db.models import Sum
from rest_framework import serializers

from films.models import *


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


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class FilmSerializer(serializers.ModelSerializer):
    review_rating_sum = serializers.SerializerMethodField(read_only=True)
    review_count = serializers.SerializerMethodField(read_only=True)
    article_rating_sum = serializers.SerializerMethodField(read_only=True)
    article_count = serializers.SerializerMethodField(read_only=True)
    tags = TagSerializer(many=True)
    directors = DirectorSerializer(many=True)
    actors = ActorSerializer(many=True)
    language = LanguageSerializer()
    country = CountrySerializer()

    class Meta:
        model = Film
        fields = '__all__'

    def get_review_count(self, obj):
        return obj.review_set.count()

    def get_article_count(self, obj):
        return obj.article_set.count()

    def get_review_rating_sum(self, obj):
        return obj.review_set.aggregate(Sum('rating'))['rating__sum'] or 0

    def get_article_rating_sum(self, obj):
        return obj.article_set.aggregate(Sum('rating'))['rating__sum'] or 0
