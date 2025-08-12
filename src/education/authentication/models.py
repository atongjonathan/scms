from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from .storages_backends import R2UserImageStorage

phone_validator = RegexValidator(
    regex=r'^\+?\d{9,15}$',
    message="Enter a valid international phone number (e.g. +254712345678)"
)


class EUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(_("first name"), max_length=150)
    user_image = models.ImageField(
        upload_to='scms_user_images/', storage=R2UserImageStorage(), blank=True)
    USERNAME_FIELD = 'email'
    middle_name = models.CharField(
        _("middle name"), max_length=150, blank=True, null=False)
    mobile_number = models.CharField(
        max_length=16, validators=[phone_validator], null=True, blank=True)
    REQUIRED_FIELDS = ['username', 'first_name']

    def get_absolute_url(self):
        return reverse("profile", kwargs={"email": self.email})

    @property
    def full_name(self):
        "Returns the user's full name."
        return self.get_full_name()

    def __str__(self):
        return self.username
