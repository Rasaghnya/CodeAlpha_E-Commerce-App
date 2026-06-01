from django.shortcuts import render

# Create your views here.


from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Cart
from .models import CartItem

from store.models import Product

@login_required
def add_to_cart(request, product_id):
    """
    Add product to user's cart.
    """

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("cart")

@login_required
def remove_from_cart(request, item_id):
    """
    Remove item from cart.
    """

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.delete()

    return redirect("cart")

@login_required
def update_cart(request, item_id):
    """
    Update quantity.
    """

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    quantity = int(
        request.POST.get(
            "quantity",
            1
        )
    )

    if quantity > 0:
        item.quantity = quantity
        item.save()

    return redirect("cart")

@login_required
def cart_view(request):
    """
    Show cart contents.
    """

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = cart.items.select_related(
        "product"
    )

    total = sum(
        item.total_price
        for item in items
    )

    context = {
        "cart": cart,
        "items": items,
        "total": total
    }

    return render(
        request,
        "orders/cart.html",
        context
    )