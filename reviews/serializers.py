from rest_framework import serializers
from .models import Review, Favorite
from users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='user.userprofile', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'user_profile', 'film', 'comment', 'rating', 'time']


class FavoriteSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='user.userprofile', read_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'user_profile', 'film', 'time']
