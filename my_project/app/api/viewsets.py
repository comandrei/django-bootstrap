from rest_framework.viewsets import ModelViewSet

from ..models import Produs, Producator

from .serializers import ProdusSerializer, ProducatorSerializer

class ProdusViewSet(ModelViewSet):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer


class ProducatorViewSet(ModelViewSet):
    queryset = Producator.objects.all()
    serializer_class = ProducatorSerializer