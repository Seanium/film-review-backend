from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Review, Favorite
from .serializers import ReviewSerializer, FavoriteSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    电影的评论
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    收藏电影
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class UserReviewsAPIView(APIView):
    """
    用户的评论
    """

    def get(self, request, user_id):
        """
        获取用户的评论
        """
        reviews = Review.objects.filter(user_id=user_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class UserFavoritesAPIView(APIView):
    """
    用户的收藏
    """
    def get(self, request, user_id):
        """
        获取用户的收藏
        """
        favorites = Favorite.objects.filter(user_id=user_id)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)


class FilmReviewsAPIView(APIView):
    """
    电影的评论
    """
    def get(self, request, film_id):
        """
        获取电影的评论
        """
        reviews = Review.objects.filter(film_id=film_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class FilmFavoritesAPIView(APIView):
    """
    电影的收藏
    """
    def get(self, request, film_id):
        """
        获取电影的收藏
        """
        favorites = Favorite.objects.filter(film_id=film_id)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)
