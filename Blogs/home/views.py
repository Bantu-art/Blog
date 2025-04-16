from django.shortcuts import render
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # latest first
    return render(request, 'home/home.html', {'posts': posts})