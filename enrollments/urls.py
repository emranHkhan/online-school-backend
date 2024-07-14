from django.urls import path
from .views import (
    EnrollmentList, EnrollmentListByStudent
)

urlpatterns = [
    path('enrollments/', EnrollmentList.as_view(), name='enrollment-list'), 
    path('enrollments/student/<int:student_id>/', EnrollmentListByStudent.as_view(), name='enrollments-by-student'),
]
