"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Admin site
    path("admin/", admin.site.urls),
    # Including categories app URLs
    path("api/v1/categories/", include("categories.urls")),
    # Including rooms app URLs
    path("api/v1/rooms/", include("rooms.urls")),
    # Including experiences app URLs
    path("api/v1/experiences/", include("experiences.urls")),
    # Including medias app URLs
    path("api/v1/medias/", include("medias.urls")),
    # Including wishlits app URLs
    path("api/v1/wishlists/", include("wishlists.urls")),
    # Including users app URLs
    path("api/v1/users/", include("users.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
