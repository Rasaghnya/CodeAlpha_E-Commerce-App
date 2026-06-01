# accounts/signals.py

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import CustomerProfile


@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    """
    Automatically create a CustomerProfile
    whenever a new User is created.
    """

    if created:
        CustomerProfile.objects.create(
            user=instance
        )


@receiver(post_save, sender=User)
def save_customer_profile(sender, instance, **kwargs):
    """
    Save profile whenever User is saved.
    """

    instance.profile.save()