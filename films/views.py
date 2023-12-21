from django.db.models import Avg
from rest_framework import viewsets, generics
from rest_framework.authtoken.models import Token
from rest_framework.generics import get_object_or_404
from rest_framework import filters

from films.filters import FilmSearchFilter
from films.models import Film, Tag, Director, Actor
from films.serializers import FilmSerializer, TagSerializer, DirectorSerializer, ActorSerializer
from reviews.models import Favorite


class FilmViewSet(viewsets.ReadOnlyModelViewSet):
    """
    电影
    """
    # 查询集还包含该电影的平均评分
    queryset = Film.objects.annotate(average_rating=Avg('review__rating'))
    serializer_class = FilmSerializer
    filter_backends = [FilmSearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'tags__name', 'directors__name', 'actors__name', 'language__name', 'country__name']


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    """
    电影标签
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [filters.OrderingFilter]


class DirectorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    导演
    """
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filter_backends = [filters.OrderingFilter]


class ActorViewSet(viewsets.ReadOnlyModelViewSet):
    """
    演员
    """
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filter_backends = [filters.OrderingFilter]


class FilmRecommendView(generics.ListAPIView):
    """
    推荐的电影。若传入有效的 token，则根据用户喜好推荐电影；否则返回全部电影
    """
    serializer_class = FilmSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        # 检查是否传入了有效的 token
        authorization_header = self.request.headers.get('Authorization')
        if authorization_header:
            token = authorization_header.split(' ')[1]
            try:
                user = Token.objects.get(key=token).user
                # 根据用户喜好推荐电影
                favorite_films = Favorite.objects.filter(user=user).values_list('film', flat=True)
                queryset = Film.objects.filter(tags__films__in=favorite_films).distinct()
                return queryset
            except (Token.DoesNotExist, IndexError):
                pass

        # 如果 token 不存在或无效，则返回全部电影
        return Film.objects.all()


class ActorFilmViewSet(viewsets.ReadOnlyModelViewSet):
    """
    该演员的全部电影
    """
    serializer_class = FilmSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        actor_id = self.kwargs['actor_id']
        actor = get_object_or_404(Actor, pk=actor_id)
        return actor.films.all()


class DirectorFilmViewSet(viewsets.ReadOnlyModelViewSet):
    """
    该导演的全部电影
    """
    serializer_class = FilmSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        director_id = self.kwargs['director_id']
        director = get_object_or_404(Director, pk=director_id)
        return director.films.all()


class TagFilmViewSet(viewsets.ReadOnlyModelViewSet):
    """
    标签下的全部电影
    """
    serializer_class = FilmSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        tag_id = self.kwargs['tag_id']
        tag = get_object_or_404(Tag, pk=tag_id)
        return tag.films.all()
