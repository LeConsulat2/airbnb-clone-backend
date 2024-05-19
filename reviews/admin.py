from typing import Any, List, Tuple
from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):

    title = "Filter by words!"
    parameter_name = "review_text"

    def lookups(self, request, model_admin) -> List[Tuple[str, str]]:
        return [
            ("excellent", "Excellent"),
            ("awesome", "Awesome"),
            ("good", "Good"),
            ("bad", "Bad"),
            ("awful", "Awful"),
        ]

    def queryset(self, request, queryset):
        if self.value():
            keyword = self.value()
            if keyword == "excellent":
                return queryset.filter(payload__isnull=True) | queryset.filter(
                    payload__icontains="excellent"
                )
            if keyword == "awesome":
                return queryset.filter(payload__isnull=True) | queryset.filter(
                    payload__icontains="awesome"
                )
            if keyword == "good":
                return queryset.filter(payload__isnull=True) | queryset.filter(
                    payload__icontains="good"
                )
            if keyword == "bad":
                return queryset.filter(payload__isnull=True) | queryset.filter(
                    payload__icontains="bad"
                )
            if keyword == "awful":
                return queryset.filter(payload__isnull=True) | queryset.filter(
                    payload__icontains="awful"
                )
        return queryset


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__category",
        "room__pet_friendly",
    )
