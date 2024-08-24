from django.db import models

from post.models import Post
from social_media_API.settings import AUTH_USER_MODEL


class Like(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} liked {self.post.id}"
