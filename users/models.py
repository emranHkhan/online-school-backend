from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, blank=True, null=True)
    image = models.URLField(blank=True, null=True)  
    is_active = models.BooleanField(default=False)  
    is_staff = models.BooleanField(default=False)   

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
    )

    objects = CustomUserManager()  

    class Meta:
        app_label = 'users'


