from django.db import models
from users.models import User
from courses.models import Course  # Explicit relative import

class Enrollment(models.Model):
    student = models.ForeignKey(
        User,
        limit_choices_to={'role': 'student'},
        on_delete=models.CASCADE
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.course}"
