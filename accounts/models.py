from django.db import models

from django.contrib.auth.models import User

# CustomerProfile Model
# accounts/models.py

class CustomerProfile(models.Model):
    """
    Stores additional information about a customer.
    Django User stores:
    - username
    - email
    - password
    This model stores:
    - address
    - phone
    - city
    - state
    - pincode
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    phone = models.CharField(max_length=15,blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100,blank=True)
    state = models.CharField(max_length=100,blank=True)
    zipcode = models.CharField(max_length=10,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
