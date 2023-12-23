from django.db.models import Case, When, Value, IntegerField
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
    queryset = Film.objects.all()
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
    推荐的电影。若传入用户id，根据用户喜好推荐电影；若未传入用户id，则返回全部电影
    """
    serializer_class = FilmSerializer
    filter_backends = [filters.OrderingFilter]

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            try:
                user = Token.objects.get(user=user_id).user
                # 根据用户喜好推荐电影
                favorite_films = Favorite.objects.filter(user=user).values_list('film', flat=True)
                favorite_films_queryset = Film.objects.filter(id__in=favorite_films)
                tail_films = Film.objects.exclude(id__in=favorite_films)
                # 创建Case语句来排序电影
                ordering = Case(
                    *[When(pk=pk, then=Value(i)) for i, pk in enumerate(favorite_films)],
                    default=Value(len(favorite_films)),
                    output_field=IntegerField()
                )
                # 合并并排序
                queryset = (favorite_films_queryset | tail_films).order_by(ordering)
                return queryset
            except (Token.DoesNotExist, IndexError):
                pass
        else:
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
