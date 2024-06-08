from rest_framework.test import APITestCase
from . import models
from rest_framework import status  # Importing the entire status module


class TestAmenities(APITestCase):

    NAME = "Amenity Test"
    DESC = "Amenity Des"
    URL = "/api/v1/rooms/amenities/"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_all_amenities(self):
        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            "Status code isn't 200",
        )
        self.assertIsInstance(data, list)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["name"], self.NAME)
        self.assertEqual(data[0]["description"], self.DESC)

    def test_create_amenity(self):
        new_amenity_name = "New Amenity"
        new_amenity_description = "New Amenity description"

        response = self.client.post(
            self.URL,
            data={
                "name": new_amenity_name,
                "description": new_amenity_description,
            },
            content_type="application/json",
        )
        data = response.json()

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED,
            "Not 201 status code",
        )
        self.assertEqual(
            data["name"],
            new_amenity_name,
        )
        self.assertEqual(
            data["description"],
            new_amenity_description,
        )


class TestAmenity(APITestCase):

    NAME = "Test Amenity"
    DESC = "Test Description"

    def setUp(self):
        models.Amenity.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_get_amenity(self):
        response = self.client.get("/api/v1/rooms/amenities/2/")
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
        )

        response = self.client.get("/api/v1/rooms/amenities/1/")
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
        )

        data = response.json()
        self.assertEqual(
            data["name"],
            self.NAME,
        )
        self.assertEqual(
            data["description"],
            self.DESC,
        )

    def test_put_amenity(self):
        updated_name = "Updated Amenity"
        updated_description = "Updated description"
        response = self.client.put(
            "/api/v1/rooms/amenities/1/",
            data={
                "name": updated_name,
                "description": updated_description,
            },
            content_type="application/json",
        )
        print(f"Status Code (PUT): {response.status_code}")
        print(f"Response Content (PUT): {response.content}")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        data = response.json()
        self.assertEqual(data["name"], updated_name)
        self.assertEqual(data["description"], updated_description)

    def test_delete_amenity(self):
        response = self.client.delete("/api/v1/rooms/amenities/1/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
