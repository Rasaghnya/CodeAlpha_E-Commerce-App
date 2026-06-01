from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Cart,CartItem,Order,OrderItem
# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ("user","created_at")
#     search_fields = ("user__username",)
#     list_filter = ("created_at",)

# @admin.register(CartItem)
# class CartItemAdmin(admin.ModelAdmin):
#     list_display = ("cart","product","quantity")
#     search_fields = ("cart__user__username","product__name")
#     list_filter = ("cart__user__username",)

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ("user","total_amount","status","created_at")
#     search_fields = ("user__username","status")
#     list_filter = ("status","created_at")

# @admin.register(OrderItem)
# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ("order","product","quantity")
#     search_fields = ("order__user__username","product__name")
#     list_filter = ("order__user__username",)


admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)