from rest_framework import serializers
from users.models import User
from courses.models import Course
from .models import Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='student'))
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    student_info = serializers.SerializerMethodField(read_only=True)
    course_info = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_at', 'student_info', 'course_info']

    def get_student_info(self, obj):
        student = obj.student
        return {
            "first_name": student.first_name,
            "last_name": student.last_name,
            "email": student.email,
        }

    def get_course_info(self, obj):
        course = obj.course
        return {
            "name": course.title,
            "teacher_name": course.teacher.username if course.teacher else None,
            "department": course.department.name,
            "price": course.price,
        }
    
    def validate(self, attrs):
        request = self.context.get('request')
        user = request.user
        if user.role != 'student':
            raise serializers.ValidationError("Only students can enroll in courses.")
        if attrs['student'] != user:
            raise serializers.ValidationError("You can only enroll yourself in a course.")
        if Enrollment.objects.filter(student=user, course=attrs['course']).exists():
            raise serializers.ValidationError("You are already enrolled in this course.")
        return attrs