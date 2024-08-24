from rest_framework.routers import DefaultRouter
from profile.views import ProfileViewSet


router = DefaultRouter()
router.register("", ProfileViewSet)

urlpatterns = router.urls

app_name = "profile"
