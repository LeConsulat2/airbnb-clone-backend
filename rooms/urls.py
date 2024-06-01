from django.urls import path
from . import views

urlpatterns = [
    path("", views.Rooms.as_view(), name="rooms-list"),  # List all rooms
    path(
        "amenities/", views.Amenities.as_view(), name="amenities-list"
    ),  # List all amenities
    path(
        "amenities/<int:pk>/", views.AmenityDetail.as_view(), name="amenity-detail"
    ),  # Detail of a specific amenity
    path(
        "<int:pk>/", views.RoomDetail.as_view(), name="room-detail"
    ),  # Detail of a specific room
]
