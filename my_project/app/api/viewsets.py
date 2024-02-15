from rest_framework.viewsets import ModelViewSet

from ..models import Produs, Producator, Recenzie, Intrebare

from .serializers import ProdusSerializer, ProducatorSerializer, RecenzieSerializer, IntrebareSerializer

class ProdusViewSet(ModelViewSet):
    queryset = Produs.objects.all()
    serializer_class = ProdusSerializer


class ProducatorViewSet(ModelViewSet):
    queryset = Producator.objects.all()
    serializer_class = ProducatorSerializer


class RecenzieViewSet(ModelViewSet):
    queryset = Recenzie.objects.all()
    serializer_class = RecenzieSerializer


class IntrebareViewSet(ModelViewSet):
    queryset = Intrebare.objects.all()
    serializer_class = IntrebareSerializer