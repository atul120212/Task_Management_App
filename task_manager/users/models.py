from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):  # Extending the default user model
    name = models.CharField(max_length=100, blank=False)  # Full name of the user
    email = models.EmailField(unique=True, blank=False)  # Unique email address
    mobile = models.CharField(max_length=15, unique=True, blank=False)  # Unique mobile number

    USERNAME_FIELD = 'email'  # Use email as the unique identifier for authentication
    REQUIRED_FIELDS = ['username', 'mobile']

    def __str__(self):
        return self.email
