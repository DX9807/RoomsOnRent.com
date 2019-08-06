from django.contrib import admin
from .models import Post, Comment




class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title','created_date','published_date','image')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','author','created_date')

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
