from django.contrib import admin
from user_auth import models

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','state','city','avtar')



admin.site.register(models.UserProfile,UserProfileAdmin)
admin.site.register(models.States)
admin.site.register(models.City)
