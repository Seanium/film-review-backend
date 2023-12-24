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
    list_display = ('user', 'avatar', 'nickname', 'gender', 'phone', 'occupation', 'signature', 'age', 'email',
                    'location', 'hobby')
    list_filter = ('user', 'gender', 'age', 'location')
    search_fields = ('user', 'nickname', 'gender', 'phone', 'occupation', 'signature', 'age', 'email',
                     'location', 'hobby')
    resource_class = UserProfileResource


@admin.register(admin.models.LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag',
                    'change_message')
    list_filter = ('action_time', 'user', 'content_type')
    search_fields = (
        'user__username', 'content_type__model', 'object_id', 'object_repr', 'action_flag', 'change_message')
    readonly_fields = (
        'action_time', 'user', 'content_type', 'object_id', 'object_repr', 'action_flag', 'change_message')
