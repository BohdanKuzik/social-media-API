from rest_framework.routers import DefaultRouter
from comment.views import CommentViewSet


router = DefaultRouter()
router.register("", CommentViewSet)

urlpatterns = router.urls

app_name = "comment"
