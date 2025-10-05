from django.contrib import admin
from .models import Product , Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'stock', 'is_active', 'featured', 'bestseller', 'on_sale', 'created_at', 'updated_at')
    list_filter = ('is_active', 'featured', 'bestseller', 'on_sale', 'category')
    search_fields = ('title', 'description', 'sku', 'tags', 'meta_title', 'meta_description')
    ordering = ('-created_at',)
    prepopulated_fields = {'meta_title': ('title',)}
    readonly_fields = ('created_at', 'updated_at')
    filter_horizontal = ('related_products',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'is_active', 'sort_order', 'created_at', 'updated_at')
    list_filter = ('is_active', 'parent')
    search_fields = ('name', 'description', 'meta_title', 'meta_description')
    ordering = ('sort_order', 'name')
    prepopulated_fields = {'meta_title': ('name',)}
    readonly_fields = ('created_at', 'updated_at')




admin.site.register(Category, CategoryAdmin)
