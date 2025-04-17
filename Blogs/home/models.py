from django.db import models
from django.contrib.auth.models import User

class BlogPost(models.Model):
    """
    Represents a blog post created by a user.

    Attributes:
        title (str): The title of the blog post.
        content (str): The content of the blog post.
        author (User): The user who authored the blog post.
        created_at (datetime): The timestamp when the blog post was created.
        updated_at (datetime): The timestamp when the blog post was last updated.
        likes (ManyToManyField): Users who liked the blog post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    def __str__(self):
        return self.title

    def total_likes(self):
        """
        Returns the total number of likes for the blog post.
        """
        return self.likes.count()

class Comment(models.Model):
    """
    Represents a comment on a blog post.

    Attributes:
        post (BlogPost): The blog post the comment is associated with.
        user (User): The user who made the comment.
        content (str): The content of the comment.
        parent (Comment): The parent comment if this is a reply.
        created_at (datetime): The timestamp when the comment was created.
    """
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"
