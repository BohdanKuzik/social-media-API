from django.db import models

from social_media_API.settings import AUTH_USER_MODEL


class Follow(models.Model):
    follower = models.ForeignKey(
        AUTH_USER_MODEL, related_name="following", on_delete=models.CASCADE
    )
    following = models.ForeignKey(
        AUTH_USER_MODEL, related_name="followers", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.follower.email} follows {self.following.email}"
