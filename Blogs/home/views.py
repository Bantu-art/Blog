from django.shortcuts import render
from .models import BlogPost
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogPostForm  # We'll create this form next

def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')  # latest first
    return render(request, 'home/home.html', {'posts': posts})

# Create Blog Post View
@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # Assign the logged-in user as the author
            blog_post.save()
            return redirect('home')  # Redirect to blog home page after successful post
    else:
        form = BlogPostForm()
    
    return render(request, 'blog/create_blog_post.html', {'form': form})
