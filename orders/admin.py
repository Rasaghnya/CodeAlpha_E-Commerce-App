from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Cart,CartItem,Order,OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

admin.site.register(OrderItem)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "total_amount",
        "status",
        "is_paid",
        "created_at",
    )

    list_filter = (
        "status",
        "is_paid",
        "created_at",
    )

    search_fields = (
        "user__username",
        "phone_number",
    )

    list_editable = (
        "status",
        "is_paid",
    )

    inlines = [
        OrderItemInline
    ]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "user",
        "created_at",
    )

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "cart",
        "product",
        "quantity",
    )
