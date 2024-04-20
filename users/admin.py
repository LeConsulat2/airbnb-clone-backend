from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "profile_photo",
                    "username",
                    "password",
                    "name",
                    "email",
                    "is_host",
                    "gender",
                    "language",
                    "currency",
                ),
                "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            ("Important dates"),
            {"fields": ("last_login", "date_joined"), "classes": ("collapse",)},
        ),
    )

    list_display = ("username", "email", "name", "is_host")

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj=obj)
        if obj and not obj.is_host:
            for fieldset in fieldsets:
                if fieldset[0] == "Profile" and "houses" in fieldset[1]["fields"]:
                    fieldset[1]["fields"] = [
                        field for field in fieldset[1]["fields"] if field != "houses"
                    ]
        return fieldsets
