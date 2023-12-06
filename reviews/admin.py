from django.contrib import admin

from reviews.models import *


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'film', 'comment', 'rating', 'time')
    list_filter = ('user', 'film', 'rating', 'time')
    search_fields = ('user', 'film', 'rating', 'time')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'film', 'time')
    list_filter = ('user', 'film', 'time')
    search_fields = ('user', 'film', 'time')
