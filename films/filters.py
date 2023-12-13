from rest_framework import filters


class FilmSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('name_only'):
            return ['name']
        elif request.query_params.get('tags_only'):
            return ['tags__name']
        elif request.query_params.get('directors_only'):
            return ['directors__name']
        elif request.query_params.get('actors_only'):
            return ['actors__name']
        elif request.query_params.get('language_only'):
            return ['language__name']
        elif request.query_params.get('country_only'):
            return ['country__name']
        return super(FilmSearchFilter, self).get_search_fields(view, request)
