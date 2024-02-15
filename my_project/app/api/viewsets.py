from rest_framework.viewsets import ModelViewSet

from ..models import Produs

from .serializers import ProdusSerializer

class ProdusViewSet(ModelViewSet):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer