from rest_framework import routers
from .viewsets import SmallProjectViewSet, BigProjectViewSet

router = routers.SimpleRouter()
router.register('small_project', SmallProjectViewSet)
router.register('big_project', BigProjectViewSet)
urlpatterns = router.urls