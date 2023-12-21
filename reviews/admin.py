from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from reviews.models import *


# Register your models here.
class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'film', 'content', 'rating', 'time')
    list_filter = ('user', 'film', 'rating', 'time')
    search_fields = ('user', 'film', 'rating', 'time')
    resource_class = ReviewResource


class FavoriteResource(resources.ModelResource):
    class Meta:
        model = Favorite


@admin.register(Favorite)
class FavoriteAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'film', 'time')
    list_filter = ('user', 'film', 'time')
    search_fields = ('user', 'film', 'time')
    resource_class = FavoriteResource


class ReviewLikeResource(resources.ModelResource):
    class Meta:
        model = ReviewLike


@admin.register(ReviewLike)
class ReviewLikeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'review', 'time')
    list_filter = ('user', 'review', 'time')
    search_fields = ('user', 'review', 'time')
    resource_class = ReviewLikeResource


class ReviewCommentResource(resources.ModelResource):
    class Meta:
        model = ReviewComment


@admin.register(ReviewComment)
class ReviewCommentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'review', 'content', 'time')
    list_filter = ('user', 'review', 'time')
    search_fields = ('user', 'review', 'time')
    resource_class = ReviewCommentResource


class ArticleResource(resources.ModelResource):
    class Meta:
        model = Article


@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'film', 'content', 'time')
    list_filter = ('user', 'film', 'time')
    search_fields = ('user', 'film', 'time')
    resource_class = ArticleResource


class ArticleLikeResource(resources.ModelResource):
    class Meta:
        model = ArticleLike


@admin.register(ArticleLike)
class ArticleLikeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'article', 'time')
    list_filter = ('user', 'article', 'time')
    search_fields = ('user', 'article', 'time')
    resource_class = ArticleLikeResource


class ArticleCommentResource(resources.ModelResource):
    class Meta:
        model = ArticleComment


@admin.register(ArticleComment)
class ArticleCommentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'user', 'article', 'content', 'time')
    list_filter = ('user', 'article', 'time')
    search_fields = ('user', 'article', 'time')
    resource_class = ArticleCommentResource
