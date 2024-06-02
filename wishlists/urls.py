from django.urls import path
from .views import Wishlists, WishlistDetail, WishlistToggle

urlpatterns = [
    path("", Wishlists.as_view()),
]
