# blogapp/urls.py

from django.urls import path
from . import views 
from .views import signup, login_view, blog_detail, blog_list, add_comment, search_blogs,share_blog  

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('', blog_list, name='blog_list'),
    path('blog/<int:blog_id>/', blog_detail, name='blog_detail'), 
    path('blog/<int:blog_id>/add_comment/', add_comment, name='add_comment'),  
    path('comment/<int:comment_id>/like/', views.like_comment, name='like_comment'),  
    path('search/', search_blogs, name='search'),  
    path('blog/share/<int:blog_id>/', share_blog, name='share_blog'),
]
