from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from django.contrib import admin
from .models import Product,Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = (
        "id",
        "name",
        "slug",
    )

    search_fields = ("name",)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
    "id",
    "image_preview",
    "name",
    "category",
    "price",
    "stock",
    "available",
    )
    list_filter = (
        "available",
        "category",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }
    list_editable = (
        "price",
        "stock",
        "available",
    )

    def image_preview(self, obj):

        if obj.image:

            return format_html(
                '<img src="{}" width="60" />',
                obj.image.url
            )

        return "No Image"


