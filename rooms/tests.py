import json
from rest_framework.test import APITestCase
from rooms import models
from categories.models import Category  # Import Category from the correct module
from rest_framework import status
from users.models import User


class TestRooms(APITestCase):

    def setUp(self):
        # Create and authenticate a test user
        self.user = User.objects.create_user(username="test", password="123")
        self.client.login(username="test", password="123")

    def test_create_room(self):
        # Test unauthenticated request
        self.client.logout()
        response = self.client.post("/api/v1/rooms/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.client.login(username="test", password="123")

        # Create necessary data for creating a room
        category = Category.objects.create(name="Test Category")
        amenity = models.Amenity.objects.create(
            name="Test Amenity", description="Test Description"
        )

        room_data = {
            "name": "Test Room",
            "description": "Test Room Description",
            "category": category.pk,
            "amenities": [amenity.pk],
            "price": 100,
            "beds": 1,
            "baths": 1,
            "check_in": "14:00",
            "check_out": "11:00",
            "country": "Test Country",
            "city": "Test City",
            "rooms": 1,
            "toilets": 1,
            "address": "123 Test St",
            "kind": "private_room",
        }

        print(f"Data being sent in POST request: {json.dumps(room_data, indent=4)}")

        response = self.client.post(
            "/api/v1/rooms/",
            data=json.dumps(room_data),  # Serialize data to JSON format
            content_type="application/json",
        )
        print(f"Status Code (POST Room): {response.status_code}")
        print(f"Response Content (POST Room): {response.content.decode('utf-8')}")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response_data = response.json()
        self.assertEqual(response_data["name"], room_data["name"])
        self.assertEqual(response_data["description"], room_data["description"])
