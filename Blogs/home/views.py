from django.shortcuts import render
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # latest first
    return render(request, 'blog/home.html', {'posts': posts})