from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    course_count = serializers.SerializerMethodField()
    is_active = serializers.BooleanField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'role', 'image', 'course_count', 'is_active']
        extra_kwargs = {
            'course_count': {'read_only': True},
        }

    def get_course_count(self, obj):
        if obj.role == 'teacher':
            return obj.courses_taught.count()
        return None

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        print(validated_data)
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            role=validated_data['role'],
            image=validated_data.get('image')
        )
        
        user.set_password(validated_data['password'])
        user.is_active = False 
        user.save()
        return user
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    