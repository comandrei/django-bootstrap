from rest_framework.serializers import ModelSerializer
from ..models import Produs

class ProdusSerializer(ModelSerializer):
    class Meta:
        model = Produs
        fields = "__all__"