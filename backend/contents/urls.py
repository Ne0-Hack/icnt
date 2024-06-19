from rest_framework import routers
from .views import ReviewViewSet, ArticleViewSet, WorksViewSet

router = routers.SimpleRouter()
router.register(r'reviews', ReviewViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'works', WorksViewSet)

urlpatterns = router.urls
