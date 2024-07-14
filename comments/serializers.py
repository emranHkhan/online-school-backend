from rest_framework import serializers
from comments.models import Comment
from enrollments.models import Enrollment
from users.models import User

class CommentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='student'))
    student_image = serializers.CharField(source='student.image', read_only=True)
    student_first_name = serializers.CharField(source='student.first_name', read_only=True)
    student_last_name = serializers.CharField(source='student.last_name', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'student', 'student_first_name', 'student_last_name', 'student_image', 'course', 'content', 'created_at']

    def validate(self, attrs):
        student = attrs['student']
        course = attrs['course']

        if not Enrollment.objects.filter(student=student, course=course).exists():
            raise serializers.ValidationError("You must be enrolled in the course to comment.")

        if Comment.objects.filter(student=student, course=course).exists():
            raise serializers.ValidationError("You have already commented on this course.")

        return attrs
    
    def create(self, validated_data):
        return Comment.objects.create(**validated_data)