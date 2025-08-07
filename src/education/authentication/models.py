from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
import os


class EUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_image = models.ImageField(
        upload_to='user_images/', blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name']

    @property
    def full_name(self):
        "Returns the user's full name."
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.username
