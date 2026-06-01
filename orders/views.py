from django.shortcuts import render

# Create your views here.
from .forms import CheckoutForm
from .models import Order
from .models import OrderItem

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

@login_required
def checkout_view(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = cart.items.all()

    if not items.exists():
        return redirect("cart")

    total = sum(
        item.total_price
        for item in items
    )

    if request.method == "POST":

        form = CheckoutForm(
            request.POST
        )

        if form.is_valid():

            order = Order.objects.create(
                user=request.user,

                total_amount=total,

                full_name=form.cleaned_data['full_name'],

                phone_number=form.cleaned_data['phone_number'],

                shipping_address=form.cleaned_data['shipping_address'],

                city=form.cleaned_data['city'],

                state=form.cleaned_data['state'],

                zipcode=form.cleaned_data['zipcode'],

                payment_method=form.cleaned_data['payment_method']
            )

            for item in items:

                OrderItem.objects.create(
                    order=order,

                    product=item.product,

                    quantity=item.quantity,

                    price=item.product.price
                )

            items.delete()

            return redirect(
                "order_success",
                order_id=order.id
            )

    else:

        form = CheckoutForm()

    context = {
        "form": form,
        "total": total
    }

    return render(
        request,
        "orders/checkout.html",
        context
    )

@login_required
def order_success_view(
    request,
    order_id
):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        "orders/order_success.html",
        {
            "order": order
        }
    )

@login_required
def order_history_view(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by(
        '-created_at'
    )

    return render(
        request,
        "orders/order_history.html",
        {
            "orders": orders
        }
    )

@login_required
def order_detail_view(
    request,
    order_id
):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        "orders/order_detail.html",
        {
            "order": order
        }
    )