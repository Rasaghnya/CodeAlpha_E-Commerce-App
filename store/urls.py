from django.urls import path

from .views import home, product_list, product_detail, contact

urlpatterns = [
    path('', home, name='home'),
    path('products/', product_list, name='product_list'),
    path('product/<slug:slug>/', product_detail, name='product_detail'),
    path('contact-us/', contact, name='contact_us'),
]


