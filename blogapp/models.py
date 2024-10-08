from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.contrib.postgres.indexes import GinIndex

class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()  
    class Meta:
        indexes = [
            GinIndex(fields=['title', 'body'], name='blog_gin_index', opclasses=['gin_trgm_ops', 'gin_trgm_ops']),  # Specify the operator classes for title and body
        ]

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)  

    def __str__(self):
        return f'Comment by {self.user.username} on {self.blog.title}'
