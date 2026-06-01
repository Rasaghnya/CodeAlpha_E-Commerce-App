from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cart(models.Model):
    """
    One cart per user
    """

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Cart" 

class CartItem(models.Model):
    """
    Products inside cart
    """

    cart = models.ForeignKey(Cart,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey("store.Product",on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.name}"

    @property
    def total_price(self):
        return self.product.price * self.quantity


class Order(models.Model):
    """
    Stores order information
    """

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("Shipped", "Shipped"),
        ("Delivered", "Delivered"),
        ("Cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders")
    total_amount = models.DecimalField(max_digits=10,decimal_places=2)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    shipping_address = models.TextField()
    
    phone_number = models.CharField(max_length=15)

    payment_method = models.CharField(max_length=50)

    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order #{self.id}"


class OrderItem(models.Model):
    """
    Stores products purchased
    in an order.
    """

    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")

    product = models.ForeignKey("store.Product",on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product.name

    @property
    def subtotal(self):
        return self.price * self.quantity