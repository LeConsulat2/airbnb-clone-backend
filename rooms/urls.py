from django.urls import path
from . import views

urlpatterns = [
    path("amenities/", views.Amenities.as_view(), name="amenities-list"),
    path("amenities/<int:pk>/", views.AmenityDetail.as_view(), name="amenity-detail"),
]
