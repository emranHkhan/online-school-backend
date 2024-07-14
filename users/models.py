from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
    )

    class Meta:
        app_label = 'users'

