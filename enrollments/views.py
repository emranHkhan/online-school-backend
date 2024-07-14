from rest_framework import generics
from .models import Enrollment
from .serializers import  EnrollmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

class EnrollmentList(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            "request": self.request
        })
        return context

    def perform_create(self, serializer):
        user = self.request.user
        if user.role != 'student':
            raise PermissionDenied("Only students can enroll in courses.")
        serializer.save()

class EnrollmentListByStudent(generics.ListAPIView):
    serializer_class = EnrollmentSerializer

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        return Enrollment.objects.filter(student_id=student_id)
