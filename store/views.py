from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Product


def home(request):
    categories = Category.objects.annotate(
        product_count=Count('products', filter=Q(products__available=True))
    ).order_by('name')

    return render(
        request,
        'store/home.html',
        {
            'categories': categories
        }
    )


def product_list(request):
    """
    Display all available products.
    """

    category_slug = request.GET.get('category')
    products = Product.objects.filter(
        available=True
    ).select_related('category')
    category = None

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    context = {
        "products": products,
        "category": category,
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


def contact(request):
    if request.method == "POST":
        messages.success(
            request,
            "Thanks! Your message has been sent. We will contact you soon."
        )
        return redirect("contact_us")

    return render(request, "store/contact.html")
