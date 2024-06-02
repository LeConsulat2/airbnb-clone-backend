from django.urls import path
from . import views

urlpatterns = [
    # List all rooms
    path("", views.Rooms.as_view(), name="rooms-list"),
    # List all amenities
    path("amenities/", views.Amenities.as_view(), name="amenities-list"),
    # Detail of a specific amenity
    path("amenities/<int:pk>/", views.AmenityDetail.as_view(), name="amenity-detail"),
    # Detail of a specific room
    path("<int:pk>/", views.RoomDetail.as_view(), name="room-detail"),
    # List all reviews for a specific room
    path("<int:pk>/reviews/", views.RoomReviews.as_view(), name="room-reviews"),
    # List all photos for a specific room
    path("<int:pk>/photos/", views.RoomPhotos.as_view(), name="room-photos"),
    # List all bookings for a specific room
    path("<int:pk>/bookings/", views.RoomBookings.as_view(), name="room-bookings"),
]
