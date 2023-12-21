from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from users.models import UserProfile


# Register your models here.

class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(ImportExportModelAdmin):
    list_display = ('user', 'avatar')
    list_filter = ('user',)
    search_fields = ('user',)
    resource_class = UserProfileResource
