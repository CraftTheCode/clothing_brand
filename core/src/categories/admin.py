from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "parent",
        "is_active",
        "sort_order",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_active", "parent")
    search_fields = ("name", "description", "meta_title", "meta_description")
    ordering = ("sort_order", "name")
    prepopulated_fields = {"meta_title": ("name",)}
    readonly_fields = ("created_at", "updated_at")
