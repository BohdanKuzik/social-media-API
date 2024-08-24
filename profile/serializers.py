from rest_framework import serializers

from profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "id",
            "user",
            "profile_picture",
            "bio",
            "location",
        ]
