from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import BlogPost, Comment
from .forms import BlogPostForm 

def home(request):
    """
    Renders the home page with a list of all blog posts.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered home page template with blog posts.
    """
    posts = BlogPost.objects.all().order_by('-created_at')  # latest first
    return render(request, 'home/home.html', {'posts': posts})

# Create Blog Post View
@login_required
def create_blog_post(request):
    """
    Handles the creation of a new blog post.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Redirects to the home page after successful creation.
    """
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # Assign the logged-in user as the author
            blog_post.save()
            return redirect('home')  # Redirect to blog home page after successful post
    else:
        form = BlogPostForm()
    
    return render(request, 'home/create_blog_post.html', {'form': form})

@login_required
def like_post(request, post_id):
    """
    Handles liking or unliking a blog post.

    Args:
        request: The HTTP request object.
        post_id (int): The ID of the blog post to like or unlike.

    Returns:
        JsonResponse: A JSON response with the updated like status and total likes.
    """
    post = get_object_or_404(BlogPost, id=post_id)
    if request.user in post.likes.all():
        post.likes.remove(request.user)  # Unlike if already liked
        liked = False
    else:
        post.likes.add(request.user)  # Like the post
        liked = True
    return JsonResponse({'liked': liked, 'total_likes': post.total_likes()})

@login_required
def add_comment(request, post_id):
    """
    Handles adding a comment or reply to a blog post.

    Args:
        request: The HTTP request object.
        post_id (int): The ID of the blog post to comment on.

    Returns:
        JsonResponse: A JSON response with the created comment details.
    """
    if request.method == 'POST':
        post = get_object_or_404(BlogPost, id=post_id)
        content = request.POST.get('content')
        parent_id = request.POST.get('parent_id')
        parent = Comment.objects.get(id=parent_id) if parent_id else None
        comment = Comment.objects.create(post=post, user=request.user, content=content, parent=parent)
        return JsonResponse({
            'id': comment.id,
            'content': comment.content,
            'user': comment.user.username,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'parent_id': parent_id
        })
