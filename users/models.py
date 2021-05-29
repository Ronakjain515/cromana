from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

from .manager import CustomUserManager

Gender_Choices = (
    ("MALE", "Male"),
    ("FEMALE", "Female"),
    ("OTHERS", "Others"),
)


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
    User_Role = (
        ("COMPANY", "Company"),
        ("JOBSEEKER", "JobSeeker"),
    )

    email = models.EmailField(_('email address'), unique=True,
                              error_messages={
                                  'unique': 'This email address is already associated with another account.'})
    status = models.CharField(max_length=10, choices=Status_Choice)
    role = models.CharField(max_length=15, choices=User_Role)
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


class JobSeekerModel(models.Model):
    """
    Job Seeker User Model
    """
    user        = models.ForeignKey(CustomUser, related_name='jobseeker', null=False, blank=False, on_delete=models.CASCADE)
    profilepic  = models.ImageField(upload_to="profile_pic", null=True, blank=True)
    firstname   = models.CharField(max_length=30, null=True, blank=False)
    lastname    = models.CharField(max_length=30, null=True, blank=False)
    mobileno    = models.CharField(max_length=15, null=True, blank=False)
    gender      = models.CharField(max_length=10, choices=Gender_Choices)

    def __str__(self):
        return self.firstname + " " + self.lastname


class CompanyModel(models.Model):
    """
    Company user model
    """
    user            = models.ForeignKey(CustomUser, related_name="company", null=False, blank=False, on_delete=models.CASCADE)
    image           = models.ImageField(upload_to="company_logo", null=True, blank=True)
    name            = models.CharField(max_length=50, null=True, blank=False)
    registrationno  = models.CharField(max_length=50, null=True, blank=False)
    address         = models.CharField(max_length=200, null=True, blank=False)
    mobileno        = models.CharField(max_length=15, null=True, blank=False)
    secondmobileno  = models.CharField(max_length=15, null=True, blank=True)
    gender          = models.CharField(max_length=10, choices=Gender_Choices)
    firstname       = models.CharField(max_length=30, null=True, blank=False)
    lastname        = models.CharField(max_length=30, null=True, blank=False)
    website_url     = models.URLField(null=True, blank=True)
    about           = models.CharField(max_length=1000, null=True, blank=False)

    def __str__(self):
        return self.name
