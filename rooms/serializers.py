from rest_framework import serializers
from .models import Amenity, Room
from users.serializers import UserProfileSerializer
from categories.serializers import CategorySerializer


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = "__all__"  # or ("name", "description")


class RoomDetailSerializer(serializers.ModelSerializer):

    owner = UserProfileSerializer(read_only=True)
    amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Room
        fields = "__all__"


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("pk", "name", "country", "city", "price", "rating")

    def get_rating(self, room):
        return room.rating()
