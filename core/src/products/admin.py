from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "uuid",
        "category",
        "price",
        "stock",
        "is_active",
        "featured",
        "bestseller",
        "on_sale",
        "created_at",
        "updated_at",
    )
    list_filter = ("is_active", "featured", "bestseller", "on_sale", "category")
    search_fields = (
        "title",
        "description",
        "sku",
        "tags",
        "meta_title",
        "meta_description",
    )
    ordering = ("-created_at",)
    prepopulated_fields = {"meta_title": ("title",)}
    readonly_fields = ("created_at", "updated_at")
    filter_horizontal = ("related_products",)
