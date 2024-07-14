from django.db import models
from courses.models import Course
from users.models import User

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name='comments', on_delete=models.CASCADE)
    student = models.ForeignKey(User, limit_choices_to={'role': 'student'}, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.student.username} on {self.course.title} at {self.created_at}"
    
