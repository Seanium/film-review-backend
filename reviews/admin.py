from django.contrib import admin

from reviews.models import *


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'film', 'content', 'rating', 'time')
    list_filter = ('user', 'film', 'rating', 'time')
    search_fields = ('user', 'film', 'rating', 'time')


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'film', 'time')
    list_filter = ('user', 'film', 'time')
    search_fields = ('user', 'film', 'time')


@admin.register(ReviewLike)
class ReviewLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'review', 'time')
    list_filter = ('user', 'review', 'time')
    search_fields = ('user', 'review', 'time')


@admin.register(ReviewComment)
class ReviewCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'review', 'content', 'time')
    list_filter = ('user', 'review', 'time')
    search_fields = ('user', 'review', 'time')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'film', 'content', 'time')
    list_filter = ('user', 'film', 'time')
    search_fields = ('user', 'film', 'time')


@admin.register(ArticleLike)
class ArticleLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'article', 'time')
    list_filter = ('user', 'article', 'time')
    search_fields = ('user', 'article', 'time')


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'article', 'content', 'time')
    list_filter = ('user', 'article', 'time')
    search_fields = ('user', 'article', 'time')
