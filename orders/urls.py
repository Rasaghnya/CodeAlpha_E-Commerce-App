from django.urls import path

from .views import (
    cart_view,
    add_to_cart,
    remove_from_cart,
    update_cart,
    checkout_view,
    order_success_view
)

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('checkout/', checkout_view, name='checkout'),
    path('success/<int:order_id>/', order_success_view, name='order_success'),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/', update_cart, name='update_cart'),
]
