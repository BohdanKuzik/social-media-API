from django.db import models

from social_media_API.settings import AUTH_USER_MODEL


class Profile(models.Model):
    user = models.OneToOneField(
        AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    profile_picture = models.ImageField(
        upload_to="profile_pics/", null=True, blank=True
    )
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.email
