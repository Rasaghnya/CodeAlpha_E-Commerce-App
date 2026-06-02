from django.shortcuts import render

# Create your views here.


from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

from django.contrib.auth.decorators import login_required
from types import SimpleNamespace
import time

from .models import Cart
from .models import CartItem
from .models import Order
from .forms import CheckoutForm

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


@login_required
def my_orders_view(request):
    """
    Show authenticated user's orders.
    """

    orders = Order.objects.filter(
        user=request.user
    ).order_by(
        "-created_at"
    )

    return render(
        request,
        "orders/my_orders.html",
        {
            "orders": orders
        }
    )


@login_required
def checkout_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.select_related("product")

    if not items.exists():
        return redirect("cart")

    total = sum(item.total_price for item in items)
    form = CheckoutForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        order_id = int(time.time())
        request.session["order_total"] = float(total)

        for item in items:
            product = item.product
            if product.stock >= item.quantity:
                product.stock = max(product.stock - item.quantity, 0)
                product.save()

        items.delete()
        return redirect("order_success", order_id=order_id)

    return render(
        request,
        "orders/checkout.html",
        {"form": form, "total": total}
    )


@login_required
def order_success_view(request, order_id):
    total_amount = request.session.pop("order_total", None)
    if total_amount is None:
        return redirect("home")

    order = SimpleNamespace(id=order_id, total_amount=total_amount)
    return render(
        request,
        "orders/order_success.html",
        {"order": order}
    )