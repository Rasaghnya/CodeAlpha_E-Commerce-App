from django.shortcuts import render, get_object_or_404

from .models import Product


def home(request):
    products = Product.objects.filter(
        available=True
    ).select_related('category')[:8]

    return render(
        request,
        'store/home.html',
        {'products': products}
    )


def product_list(request):
    """
    Display all available products.
    """

    products = Product.objects.filter(
        available=True
    ).select_related('category')

    context = {
        "products": products
    }

    return render(
        request,
        'store/product.html',
        context
    )


def product_detail(request, slug):
    """
    Display single product details.
    """

    product = get_object_or_404(
        Product,
        slug=slug,
        available=True
    )

    context = {
        "product": product
    }

    return render(
        request,
        "store/product_detail.html",
        context
    )