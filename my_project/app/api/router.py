from rest_framework.routers import DefaultRouter

from .viewsets import ProdusViewSet, ProducatorViewSet, RecenzieViewSet, IntrebareViewSet

router = DefaultRouter()
router.register(r'producator', ProducatorViewSet)
router.register(r'produs', ProdusViewSet)
router.register(r'recenzie', RecenzieViewSet)
router.register(r'intrebare', IntrebareViewSet)

urls = router.urls