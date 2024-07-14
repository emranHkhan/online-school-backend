from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    ordering_fields = ['title', 'created_at']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        total_count = queryset.count()

        serializer = self.get_serializer(queryset, many=True)

        response_data = {
            'total_count': total_count,
            'courses': serializer.data
        }

        return Response(response_data)

    def get_queryset(self):
        queryset = Course.objects.all()

        teacher_id = self.request.query_params.get('teacher')

        if teacher_id:
            # if not self.request.user.role == 'teacher':
            #     queryset = queryset.none()  
            #     return queryset

            # queryset = queryset.filter(teacher_id=teacher_id, teacher=self.request.user)
            queryset = queryset.filter(teacher_id=teacher_id)

        department_id = self.request.query_params.get('department')
        if department_id:
            queryset = queryset.filter(department_id=department_id)

        ordering = self.request.query_params.get('ordering')
        if ordering in self.ordering_fields:
            queryset = queryset.order_by(ordering)

        return queryset

class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "request": self.request
        })
        return context

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'teacher':
            raise PermissionDenied("Only teachers can create courses.")
        serializer.save()

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Course.objects.filter(teacher=user)
        raise PermissionDenied("Please Login to see all courses.")

    def perform_update(self, serializer):
        user = self.request.user
        if not user.is_authenticated or user.role != 'teacher':
            raise PermissionDenied("You do not have permission to edit this course.")
        if serializer.instance.teacher != user:
            raise PermissionDenied("You do not have permission to edit this course.")
        serializer.save()

    def perform_destroy(self, instance):
        user = self.request.user
        if not user.is_authenticated or user.role != 'teacher':
            raise PermissionDenied("You do not have permission to delete this course.")
        if instance.teacher != user:
            raise PermissionDenied("You do not have permission to delete this course.")
        instance.delete()
        
