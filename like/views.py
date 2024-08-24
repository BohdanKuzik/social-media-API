from rest_framework import viewsets

from like.models import Like
from like.serializers import LikeSerializer


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
