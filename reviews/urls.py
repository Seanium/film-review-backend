from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
# 收藏
router.register('favorites', FavoriteViewSet, basename='favorites')
# 短评
router.register('reviews', ReviewViewSet, basename='reviews')
router.register('review-likes', ReviewLikesViewSet, basename='review_likes')
router.register('review-comments', ReviewCommentsViewSet, basename='review_comments')
# 长评
router.register('articles', ArticleViewSet, basename='articles')
router.register('article-likes', ArticleLikesViewSet, basename='article_likes')
router.register('article-comments', ArticleCommentsViewSet, basename='article_comments')

urlpatterns = [
    path('', include(router.urls)),
    # 用户的收藏、短评、长评
    path('users/<int:user_id>/favorites/', UserFavoritesAPIView.as_view(), name='user_favorites'),
    path('users/<int:user_id>/reviews/', UserReviewsAPIView.as_view(), name='user_reviews'),
    path('users/<int:user_id>/articles/', UserArticlesAPIView.as_view(), name='user_articles'),
    # 电影的被收藏、短评、长评
    path('films/<int:film_id>/favorites/', FilmFavoritesAPIView.as_view(), name='film_favorites'),
    path('films/<int:film_id>/reviews/', FilmReviewsAPIView.as_view(), name='film_reviews'),
    path('films/<int:film_id>/articles/', FilmArticlesAPIView.as_view(), name='film_articles'),
    # 短评的点赞、评论
    path('reviews/<int:review_id>/likes/', ReviewLikesAPIView.as_view(), name='review_likes'),
    path('reviews/<int:review_id>/comments/', ReviewCommentsAPIView.as_view(), name='review_comments'),
    # 长评的点赞、评论
    path('articles/<int:article_id>/likes/', ArticleLikesAPIView.as_view(), name='article_likes'),
    path('articles/<int:article_id>/comments/', ArticleCommentsAPIView.as_view(), name='article_comments'),
]
