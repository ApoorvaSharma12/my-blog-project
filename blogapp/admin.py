from django.contrib import admin
from .models import Blog, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'body')
    list_filter = ('created_at', 'tags') 

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'blog', 'created_at', 'likes')
    search_fields = ('body',)
    list_filter = ('created_at', 'blog')
