from django.db import models
from django.contrib.auth.models import AbstractUser
from user_app.manager import CustomUserManager

class User(AbstractUser):
    username = None
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = 'email'  # Use email instead of username
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email