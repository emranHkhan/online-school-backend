from django.urls import path
from .views import (
    DepartmentList,
)

urlpatterns = [
    path('departments/', DepartmentList.as_view(), name='department-list'),
]
