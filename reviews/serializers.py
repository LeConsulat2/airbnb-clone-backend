from rest_framework import serializers
from users.serializers import UserProfileSerializer
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ("user", "payload", "rating")
