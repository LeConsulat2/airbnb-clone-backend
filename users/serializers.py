from rest_framework.serializers import ModelSerializer
from .models import User


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "avatar",
            "username",
        )
