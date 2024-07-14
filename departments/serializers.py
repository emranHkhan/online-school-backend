from rest_framework import serializers
from departments.models import Department

class DepartmentSerializer(serializers.ModelSerializer):
    course_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = ['id', 'name', 'course_count']

    def get_course_count(self, obj):
        return obj.course_set.count()