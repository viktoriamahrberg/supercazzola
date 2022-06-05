from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserProfile(models.Model):
    """
    User profile to hold shipping information, order history and wishlist
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address = models.CharField(max_length=80, null=True, blank=True)
    default_optional_address = models.CharField(max_length=80, null=True, blank=True)
    default_city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country *', null=True, blank=True) 

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def save_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Signal used to update or create a user profile 
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()


