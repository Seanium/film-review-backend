from rest_framework import viewsets, filters, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    收藏电影
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    filter_backends = [filters.OrderingFilter]


class ReviewViewSet(viewsets.ModelViewSet):
    """
    短评
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.OrderingFilter]


class ReviewLikesViewSet(viewsets.ModelViewSet):
    """
    短评点赞
    """
    queryset = ReviewLike.objects.all()
    serializer_class = ReviewLikeSerializer
    filter_backends = [filters.OrderingFilter]


class ReviewCommentsViewSet(viewsets.ModelViewSet):
    """
    短评评论
    """
    queryset = ReviewComment.objects.all()
    serializer_class = ReviewCommentSerializer
    filter_backends = [filters.OrderingFilter]


class ArticleViewSet(viewsets.ModelViewSet):
    """
    长评
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [filters.OrderingFilter]


class ArticleLikesViewSet(viewsets.ModelViewSet):
    """
    长评点赞
    """
    queryset = ArticleLike.objects.all()
    serializer_class = ArticleLikeSerializer
    filter_backends = [filters.OrderingFilter]


class ArticleCommentsViewSet(viewsets.ModelViewSet):
    """
    长评评论
    """
    queryset = ArticleComment.objects.all()
    serializer_class = ArticleCommentSerializer
    filter_backends = [filters.OrderingFilter]


class UserFavoritesAPIView(generics.ListAPIView):
    """
    用户的收藏，仅支持get
    """
    serializer_class = FavoriteSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Favorite.objects.filter(user_id=user_id)


class UserReviewsAPIView(generics.ListAPIView):
    """
    用户的短评，仅支持get
    """
    serializer_class = ReviewSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Review.objects.filter(user_id=user_id)


class UserArticlesAPIView(generics.ListAPIView):
    """
    用户的长评，仅支持get
    """
    serializer_class = ArticleSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Article.objects.filter(user_id=user_id)


class FilmFavoritesAPIView(generics.ListAPIView):
    """
    电影的被收藏记录，仅支持get
    """
    serializer_class = FavoriteSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        film_id = self.kwargs['film_id']
        return Favorite.objects.filter(film_id=film_id)


class FilmReviewsAPIView(generics.ListAPIView):
    """
    电影的短评，仅支持get
    """
    serializer_class = ReviewSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        film_id = self.kwargs['film_id']
        return Review.objects.filter(film_id=film_id)


class FilmArticlesAPIView(generics.ListAPIView):
    """
    电影的长评，仅支持get
    """
    serializer_class = ArticleSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        film_id = self.kwargs['film_id']
        return Article.objects.filter(film_id=film_id)


class ReviewLikesAPIView(generics.ListAPIView):
    """
    短评的点赞，仅支持get
    """
    serializer_class = ReviewLikeSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        review_id = self.kwargs['review_id']
        return ReviewLike.objects.filter(review_id=review_id)


class ReviewCommentsAPIView(APIView):
    """
    短评的评论，仅支持get
    """

    def get(self, request, review_id):
        review_comments = ReviewComment.objects.filter(review_id=review_id)
        serializer = ReviewCommentSerializer(review_comments, many=True)
        return Response(serializer.data)


class ArticleLikesAPIView(generics.ListAPIView):
    """
    长评的点赞，仅支持get
    """
    serializer_class = ArticleLikeSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return ArticleLike.objects.filter(article_id=article_id)


class ArticleCommentsAPIView(generics.ListAPIView):
    """
    长评的评论，仅支持get
    """
    serializer_class = ArticleCommentSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        article_id = self.kwargs['article_id']
        return ArticleComment.objects.filter(article_id=article_id)
