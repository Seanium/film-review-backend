from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('reviews', ReviewViewSet, basename='reviews')
router.register('favorites', FavoriteViewSet, basename='favorites')

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:user_id>/reviews/', UserReviewsAPIView.as_view(), name='user_reviews'),
    path('users/<int:user_id>/favorites/', UserFavoritesAPIView.as_view(), name='user_favorites'),
    path('films/<int:film_id>/reviews/', FilmReviewsAPIView.as_view(), name='film_reviews'),
    path('films/<int:film_id>/favorites/', FilmFavoritesAPIView.as_view(), name='film_favorites'),
]
