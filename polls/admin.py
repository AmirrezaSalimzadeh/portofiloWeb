from django.contrib import admin
from .models import Quotes

@admin.register(Quotes)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("content", "author", "created_at", "featured")
    list_display_links = ("content",)
    list_editable = ("featured",)
    ordering = ("-created_at",)
    list_per_page = 20

    search_fields = ("content", "author")
    list_filter = ("author", "created_at", "featured")
    date_hierarchy = "created_at"

    readonly_fields = ("created_at",)

    fieldsets = (
        ("Quote Details", {"fields": ("content", "author")}),
        ("Metadata", {"fields": ("created_at", "featured")}),
    )

    actions = ["mark_as_featured"]

    def mark_as_featured(self, request, queryset):
        queryset.update(featured=True)
    mark_as_featured.short_description = "Mark selected quotes as featured"

