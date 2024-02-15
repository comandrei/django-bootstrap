from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from ..models import Produs, Producator

class ProdusSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Produs
        fields = "__all__"
        depth = 1

    total_stoc = SerializerMethodField()

    def get_total_stoc(self, obj):
        return obj.pret * obj.stoc

class ProducatorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Producator
        fields = "__all__"