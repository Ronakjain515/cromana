from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Class for creating models for users.
    """

    Status_Choice = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
        ('PENDING', 'Pending'),
        ('DELETED', 'Deleted')
    )

    email = models.EmailField(_('email address'), unique=True,
                              error_messages={
                                  'unique': 'This email address is already associated with another account.'})
    status = models.CharField(max_length=10, choices=Status_Choice)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    objects = CustomUserManager()

    def __str__(self):
        """
        Function to return email.
        """
        return self.email
