from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Product,Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ("name","category","price","stock","available","created_at")
#     search_fields = ("name","category__name")
#     list_filter = ("available","created_at")

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ("name","slug")
#     search_fields = ("name",)
#     list_filter = ("name",)

admin.site.register(Product)

