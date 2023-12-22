from rest_framework import serializers
from .models import *
from users.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='user.userprofile', read_only=True)
    like_count = serializers.IntegerField(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'user', 'user_profile', 'film', 'content', 'rating', 'time', 'watched', 'like_count',
                  'comment_count']


class FavoriteSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='user.userprofile', read_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'user', 'user_profile', 'film', 'time']


class ReviewLikeSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='user.userprofile', read_only=True)

    class Meta:
        model = ReviewLike
        fields = ['id', 'user', 'user_profile', 'review', 'time']


class ReviewCommentSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='user.userprofile', read_only=True)

    class Meta:
        model = ReviewComment
        fields = ['id', 'user', 'user_profile', 'review', 'content', 'time']


class ArticleSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='user.userprofile', read_only=True)
    like_count = serializers.IntegerField(read_only=True)
    comment_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'user', 'user_profile', 'film', 'rating', 'title', 'content', 'time', 'spoiler',
                  'privacy', 'original', 'like_count', 'comment_count']


class ArticleLikeSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='user.userprofile', read_only=True)

    class Meta:
        model = ArticleLike
        fields = ['id', 'user', 'user_profile', 'article', 'time']


class ArticleCommentSerializer(serializers.ModelSerializer):
    user_profile = UserProfileSerializer(source='user.userprofile', read_only=True)

    class Meta:
        model = ArticleComment
        fields = ['id', 'user', 'user_profile', 'article', 'content', 'time']
