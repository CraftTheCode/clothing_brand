import uuid
from django.db import models
from categories.models import Category


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="products"
    )
    stock = models.PositiveIntegerField()
    sku = models.CharField(max_length=100, unique=True)
    image_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    tags = models.CharField(
        max_length=255, blank=True, null=True
    )  # Comma-separated tags
    rating = models.FloatField(default=0.0)
    num_reviews = models.PositiveIntegerField(default=0)
    featured = models.BooleanField(default=False)
    bestseller = models.BooleanField(default=False)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )
    sort_order = models.IntegerField(default=0)
    available_from = models.DateTimeField(blank=True, null=True)
    available_to = models.DateTimeField(blank=True, null=True)
    dimensions = models.CharField(
        max_length=100, blank=True, null=True
    )  # e.g., "10x20x30 cm"
    color = models.CharField(max_length=50, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)  # e.g., "S, M, L, XL"
    material = models.CharField(max_length=100, blank=True, null=True)
    shipping_details = models.TextField(blank=True, null=True)
    return_policy = models.TextField(blank=True, null=True)
    related_products = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.title
