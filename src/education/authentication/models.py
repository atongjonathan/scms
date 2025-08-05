from django.contrib.auth.models import AbstractUser
from django.db import models


class EUser(AbstractUser):
    email = models.EmailField(unique=True)
    user_image = models.ImageField(upload_to='user_images/', blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
