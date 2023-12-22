from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from films.models import *


# Register your models here.
class FilmResource(resources.ModelResource):
    class Meta:
        model = Film
        fields = ('id', 'name', 'duration', 'release_date', 'info', 'cover', 'tags', 'directors', 'actors', 'language',
                  'country')


@admin.register(Film)
class FilmAdmin(ImportExportModelAdmin):
    list_display = (
        'id', 'name', 'duration', 'release_date', 'info', 'cover', 'display_tags', 'display_directors',
        'display_actors', 'language',
        'country')
    list_filter = ('name', 'duration', 'release_date', 'tags', 'language', 'country')
    search_fields = ('name', 'duration', 'release_date', 'tags', 'language', 'country')

    def display_tags(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all())

    def display_directors(self, obj):
        return ', '.join(director.name for director in obj.directors.all())

    def display_actors(self, obj):
        return ', '.join(actor.name for actor in obj.actors.all())

    display_tags.short_description = 'Tags'
    resource_class = FilmResource


class TagResource(resources.ModelResource):
    class Meta:
        model = Tag


@admin.register(Tag)
class TagAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)
    resource_class = TagResource


class DirectorResource(resources.ModelResource):
    class Meta:
        model = Director


@admin.register(Director)
class DirectorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'photo', 'birth_date', 'birth_place', 'info')
    list_filter = ('name', 'birth_date', 'birth_place')
    search_fields = ('name',)
    resource_class = DirectorResource


class ActorResource(resources.ModelResource):
    class Meta:
        model = Actor


@admin.register(Actor)
class ActorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'photo', 'birth_date', 'birth_place', 'info')
    list_filter = ('name', 'birth_date', 'birth_place')
    search_fields = ('name',)
    resource_class = ActorResource


class LanguageResource(resources.ModelResource):
    class Meta:
        model = Language


@admin.register(Language)
class LanguageAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)
    resource_class = LanguageResource


class CountryResource(resources.ModelResource):
    class Meta:
        model = Country


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)
    resource_class = CountryResource
