from django.urls import path
from .views import (
    UserList, UserDetail,
    UserRegistrationView, UserLoginApiView, UserLogoutApiView, ActivateAccountView, TeacherList
)

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('teachers/', TeacherList.as_view(), name='teacher-list'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginApiView.as_view(), name='login'),
    path('logout/', UserLogoutApiView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', ActivateAccountView.as_view(), name='activate'),
]
