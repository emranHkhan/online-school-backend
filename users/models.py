from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, blank=True, null=True)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)  # Change URLField to ImageField
    is_active = models.BooleanField(default=False)  # Default to False for new users
    is_staff = models.BooleanField(default=False)   # Default to False for new users

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
    )

    objects = CustomUserManager()  # Use custom user manager

    class Meta:
        app_label = 'users'


