from rest_framework.serializers import HyperlinkedModelSerializer
from ..models import Produs, Producator

class ProdusSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Produs
        fields = "__all__"
        depth = 1

    

class ProducatorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Producator
        fields = "__all__"