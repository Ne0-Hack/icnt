from rest_framework import routers
from .views import OrderViewSet, ServiceViewSet


router = routers.SimpleRouter()
router.register(r'order', OrderViewSet)
router.register(r'service', ServiceViewSet)

urlpatterns = router.urls
