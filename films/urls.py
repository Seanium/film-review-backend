from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.routers import DefaultRouter

from db_backend import settings
from films.views import *

router = DefaultRouter()
router.register(r'films', FilmViewSet, basename='film')
router.register(r'tags', TagViewSet, basename='tag')
router.register(r'directors', DirectorViewSet, basename='director')
router.register(r'actors', ActorViewSet, basename='actor')

urlpatterns = [
    path('', include(router.urls)),
    path('recommend/', FilmRecommendView.as_view(), name='film-recommend'),
    path('actors/<int:actor_id>/films/', ActorFilmViewSet.as_view({'get': 'list'}), name='actor-films'),
    path('directors/<int:director_id>/films/', DirectorFilmViewSet.as_view({'get': 'list'}), name='director-films'),
    path('tags/<int:tag_id>/films/', TagFilmViewSet.as_view({'get': 'list'}), name='tag-films'),
    # 媒体文件
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media')
]
