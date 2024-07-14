from rest_framework import serializers
from comments.serializers import CommentSerializer
from users.serializers import UserSerializer
from users.models import User
from departments.models import Department
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='teacher'), write_only=True)
    teacher_name = serializers.SerializerMethodField(read_only=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    department_name = serializers.SerializerMethodField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    students = UserSerializer(many=True, read_only=True)
    teacher_image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'teacher', 'teacher_name', 'teacher_image', 'department', 'department_name', 'price', 'created_at', 'comments', 'students']

    def get_teacher_name(self, obj):
        return obj.teacher.username if obj.teacher else None
    
    def get_department_name(self, obj):
        return obj.department.name if obj.department else None
    
    def get_teacher_image(self, obj):
        return obj.teacher.image if obj.teacher else None
    
    def validate_teacher(self, value):
        request = self.context.get('request')
        user = request.user
        if value != user:
            raise serializers.ValidationError("You can only assign yourself as the teacher for this course.")
        return value

    def create(self, validated_data):
        validated_data['teacher'] = self.context['request'].user
        return super().create(validated_data)