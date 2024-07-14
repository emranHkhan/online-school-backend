from django.db import models
from users.models import User
from departments.models import Department

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    teacher = models.ForeignKey(
        User,
        limit_choices_to={'role': 'teacher'},
        related_name='courses_taught',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(
        User,
        through='enrollments.Enrollment',
        related_name='courses_enrolled'
    )

    def __str__(self):
        return self.title
