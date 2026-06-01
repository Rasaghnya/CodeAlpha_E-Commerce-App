from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import CustomerProfile

# @admin.register(CustomerProfile)
# class CustomerProfileAdmin(admin.ModelAdmin):
#     list_display = ("user","phone","city","state","zipcode")
#     search_fields = ("user__username","phone","city","state","zipcode")
#     list_filter = ("city","state")

admin.site.register(CustomerProfile)
