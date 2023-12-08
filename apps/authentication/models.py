"""Models for the authentication app."""
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.db.models import Model

from .managers import UserManager


class DualisUser(AbstractBaseUser, PermissionsMixin):
    """DualisUser Model
    """
    email = models.EmailField(max_length=254, unique=True, primary_key=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    last_updated = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        """Returns the url to access a particular instance of DualisUser.

        Returns:
            str: URL for DualisUser instance.
        """
        return f"/users/{self.pk}/"
