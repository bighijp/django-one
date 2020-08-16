from django.contrib import admin
#from exe01.models import users
from exe01.models import UserProfileInfo

# Register your models here.

admin.site.register(UserProfileInfo)
"""
admin.site.register(users)


@admin.register(users)

class usersAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")
"""
