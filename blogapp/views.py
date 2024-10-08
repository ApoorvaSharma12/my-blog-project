# blogapp/views.py

import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, CustomLoginForm
from .models import Blog, Comment
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.postgres.search import TrigramSimilarity
from django.core.mail import send_mail
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after signup
            return redirect('blog_list')  # Redirect to your blog list page
    else:
        form = SignUpForm()
    return render(request, 'blogapp/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog_list')  # Redirect to your blog list page
    else:
        form = CustomLoginForm()
    return render(request, 'blogapp/login.html', {'form': form})

def blog_list(request):
    blogs = Blog.objects.all().order_by('-created_at')  # Assuming you have a 'created_at' field
    paginator = Paginator(blogs, 5)  # Show 5 blogs per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blogapp/blog_list.html', {'page_obj': page_obj})

def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    comments = blog.comments.all()  # Use the related name 'comments'
    context = {
        'blog': blog,
        'comments': comments,
    }
    return render(request, 'blogapp/blog_detail.html', context)

def add_comment(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, id=blog_id)
        body = request.POST.get('body')
        comment = Comment.objects.create(user=request.user, blog=blog, body=body)
        comment.save()  # Save the comment to the database
        return redirect('blog_detail', blog_id=blog.id)  # Redirect back to the blog detail page

def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.likes += 1  # Increment the likes count
    comment.save()  # Save the updated comment
    return redirect('blog_detail', blog_id=comment.blog.id)  # Redirect back to the blog detail page

def search_blogs(request):
    query = request.GET.get('q')
    results = []

    if query:
        # Perform the trigram similarity search on title, body, and tags
        results = Blog.objects.annotate(
            similarity=TrigramSimilarity('title', query) + 
                        TrigramSimilarity('body', query) + 
                        TrigramSimilarity('tags__name', query)  # Assuming tags are a ManyToManyField with a 'name' field
        ).filter(similarity__gt=0.3).distinct().order_by('-similarity')  # Use distinct() to avoid duplicates

    return render(request, 'blogapp/search_results.html', {'results': results, 'query': query})


def share_blog(request, blog_id):
    if request.method == 'POST':
        email = request.POST.get('email')
        blog = get_object_or_404(Blog, id=blog_id)
        
       
        subject = f"Check out this blog post: {blog.title}"
        message = f"Hi there,\n\nI thought you might be interested in this blog post: {blog.title}\n\n{blog.body}\n\nYou can read it here: http://yourdomain.com/blog/{blog.id}/"  # Change the URL to your domain
        
        try:
            send_mail(subject, message, 'your_email@example.com', [email])  
            messages.success(request, 'Blog post shared successfully!')
        except Exception as e:
            messages.error(request, 'Failed to share the blog post. Please try again.')
        
        return redirect('blog_detail', blog_id=blog.id)