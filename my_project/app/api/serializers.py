from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from ..models import Produs, Producator, Recenzie, Intrebare

class RecenzieSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Recenzie
        fields = "__all__"

class IntrebareSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Intrebare
        fields = "__all__"

class ProdusSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Produs
        fields = ["titlu", "producator", "stoc", "pret", "descriere", "recenzie_set", "intrebare_set", "rating", "total_stoc"]
        depth = 1

    total_stoc = SerializerMethodField()
    rating = SerializerMethodField()

    def get_total_stoc(self, obj):
        return obj.pret * obj.stoc
    
    def get_rating(self, obj):
        return obj.rating
    

class ProducatorSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Producator
        fields = "__all__"