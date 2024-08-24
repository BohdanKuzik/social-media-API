from rest_framework import viewsets

from follow.models import Follow
from follow.serializers import FollowSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    queryset = Follow.objects.all()
