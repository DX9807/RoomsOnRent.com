from django.contrib import admin
from user_auth import models

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','state','city','avtar')



admin.site.register(models.UserProfile,UserProfileAdmin)
