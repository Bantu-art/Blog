"""
URL patterns for the home app.

Routes:
    - '' (home): Displays all blog posts.
    - 'create/': Allows users to create a new blog post.
    - 'like/<int:post_id>/': Handles liking or unliking a blog post.
    - 'comment/<int:post_id>/': Handles adding comments or replies to a blog post.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_blog_post, name='create_blog_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
]