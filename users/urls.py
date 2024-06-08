from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # Handles requests to list users or create a new user
    path("", views.Users.as_view()),
    # Handles requests to get or update the authenticated user's profile
    path("me", views.Me.as_view()),
    # Handles requests to change the authenticated user's password
    path("change-password", views.ChangePassword.as_view()),
    # Handles login requests using username and password
    path("log-in", views.LogIn.as_view()),
    # Handles logout requests, terminating the user's session
    path("log-out", views.LogOut.as_view()),
    # Handles login requests using the Django REST Framework's token authentication
    path("token-login", obtain_auth_token),
    # Handles login requests using JWT (JSON Web Token) authentication
    path("jwt-login", views.JWTLogIn.as_view()),
    # Handles requests to get the public profile of a user by their username
    path("@<str:username>", views.PublicUser.as_view()),
]
