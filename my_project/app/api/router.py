from rest_framework.routers import DefaultRouter

from .viewsets import ProdusViewSet

router = DefaultRouter()
router.register(r'produs', ProdusViewSet)

urls = router.urls