from rest_framework.serializers import ModelSerializer
from .models import Perk


class PerksSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = "__all__"
