from django.urls import path
from .views import (
    CourseList, CourseDetail, CourseCreateAPIView
)

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name='course-detail'),
    path('courses/create/', CourseCreateAPIView.as_view(), name='course-create'),
]
