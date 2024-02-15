from rest_framework.routers import DefaultRouter

from .viewsets import ProdusViewSet, ProducatorViewSet

router = DefaultRouter()
router.register(r'producator', ProducatorViewSet)
router.register(r'produs', ProdusViewSet)

urls = router.urls