from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    收藏电影
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """
    短评
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewLikesViewSet(viewsets.ModelViewSet):
    """
    短评点赞
    """
    queryset = ReviewLike.objects.all()
    serializer_class = ReviewLikeSerializer


class ReviewCommentsViewSet(viewsets.ModelViewSet):
    """
    短评评论
    """
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """
    长评
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleLikesViewSet(viewsets.ModelViewSet):
    """
    长评点赞
    """
    queryset = ArticleLike.objects.all()
    serializer_class = ArticleLikeSerializer


class ArticleCommentsViewSet(viewsets.ModelViewSet):
    """
    长评评论
    """
    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentSerializer


class UserFavoritesAPIView(APIView):
    """
    用户的收藏，仅支持get
    """

    def get(self, request, user_id):
        """
        获取用户的收藏
        """
        favorites = Favorite.objects.filter(user_id=user_id)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)


class UserReviewsAPIView(APIView):
    """
    用户的短评，仅支持get
    """

    def get(self, request, user_id):
        """
        获取用户的短评
        """
        reviews = Review.objects.filter(user_id=user_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class UserArticlesAPIView(APIView):
    """
    用户的长评，仅支持get
    """

    def get(self, request, user_id):
        """
        获取用户的长评
        """
        articles = Article.objects.filter(user_id=user_id)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class FilmFavoritesAPIView(APIView):
    """
    电影的被收藏记录，仅支持get
    """

    def get(self, request, film_id):
        """
        获取电影的被收藏记录
        """
        favorites = Favorite.objects.filter(film_id=film_id)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data)


class FilmReviewsAPIView(APIView):
    """
    电影的短评，仅支持get
    """

    def get(self, request, film_id):
        """
        获取电影的短评
        """
        reviews = Review.objects.filter(film_id=film_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class FilmArticlesAPIView(APIView):
    """
    电影的长评，仅支持get
    """

    def get(self, request, film_id):
        """
        获取电影的长评
        """
        articles = Article.objects.filter(film_id=film_id)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ReviewLikesAPIView(APIView):
    """
    短评的点赞，仅支持get
    """

    def get(self, request, review_id):
        review_likes = ReviewLike.objects.filter(review_id=review_id)
        serializer = ReviewLikeSerializer(review_likes, many=True)
        return Response(serializer.data)


class ReviewCommentsAPIView(APIView):
    """
    短评的评论，仅支持get
    """

    def get(self, request, review_id):
        review_comments = ReviewComment.objects.filter(review_id=review_id)
        serializer = ReviewCommentSerializer(review_comments, many=True)
        return Response(serializer.data)


class ArticleLikesAPIView(APIView):
    """
    长评的点赞，仅支持get
    """

    def get(self, request, article_id):
        article_likes = ArticleLike.objects.filter(article_id=article_id)
        serializer = ArticleLikeSerializer(article_likes, many=True)
        return Response(serializer.data)


class ArticleCommentsAPIView(APIView):
    """
    长评的评论，仅支持get
    """

    def get(self, request, article_id):
        article_comments = ArticleComment.objects.filter(article_id=article_id)
        serializer = ArticleCommentSerializer(article_comments, many=True)
        return Response(serializer.data)
