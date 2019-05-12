from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns around the globe.
    name = models.CharField(_("User's name"), blank=True, max_length=255)
    is_delivery_person = models.BooleanField('Delivery Person status', default=False)
    is_store_manager = models.BooleanField('Manager status', default=False)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    def get_profile_name(self):
        if self.name:
            return self.name

        return self.username
