from rest_framework.routers import DefaultRouter
from follow.views import FollowViewSet


router = DefaultRouter()
router.register("", FollowViewSet)

urlpatterns = router.urls

app_name = "follow"
