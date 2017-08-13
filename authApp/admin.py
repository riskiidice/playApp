from django.contrib import admin
from models import UserProfile
# Register your models here.

class UserProfileModelAdmin(admin.ModelAdmin):
    list_display = ['owner', 'group', 'old_school']
    search_fiels = ['owner']
    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileModelAdmin)
