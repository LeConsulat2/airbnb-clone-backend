from rest_framework.serializers import ModelSerializer
from .models import Amenity, Room
from users.serializers import UserProfileSerializer
from categories.serializers import CategorySerializer


class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"  # or ("name", "description")


class RoomDetailSerializer(ModelSerializer):

    owner = UserProfileSerializer()
    amenities = AmenitySerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = Room
        fields = "__all__"


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ("pk", "name", "country", "city", "price")
