from rest_framework.routers import DefaultRouter
from like.views import LikeViewSet


router = DefaultRouter()
router.register("", LikeViewSet)

urlpatterns = router.urls

app_name = "like"
