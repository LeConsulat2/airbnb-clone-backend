from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.see_all_rooms),
    path("<int:room_pk>", views.see_one_room),
    path("<str:room_name>", views.see_one_room),
    path("api/v1/rooms/amenities", include("rooms.urls")),
]
