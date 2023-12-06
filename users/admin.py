from django.contrib import admin
from users.models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar')
    list_filter = ('user',)
    search_fields = ('user',)
