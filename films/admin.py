from django.contrib import admin
from films.models import *


# Register your models here.
@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'duration', 'release_date', 'info', 'cover', 'display_tags')
    list_filter = ('name', 'duration', 'release_date', 'tags')
    search_fields = ('name', 'duration', 'release_date', 'tags')

    def display_tags(self, obj):
        return ', '.join(tag.name for tag in obj.tags.all())

    display_tags.short_description = 'Tags'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)
