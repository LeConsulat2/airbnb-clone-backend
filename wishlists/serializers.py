from rest_framework.serializers import ModelSerializer
from rooms.serializers import RoomListSerializer
from .models import Wishlist


class WishlistSerializer(ModelSerializer):

    rooms = RoomListSerializer(read_only=True, many=True)

    class Meta:
        model = Wishlist
        fields = ("pk", "name", "rooms")
