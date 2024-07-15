from django.contrib import admin
from django.http import HttpResponse
from django.urls import get_resolver, path, include, reverse
from django.utils.html import format_html
from django.conf import settings
from django.conf.urls.static import static

url_descriptions = {
    'user-detail': 'Detail view of a specific user',
    'department-list': 'List all departments',
    'course-list': 'List all courses (by teacher and department)',
    'course-detail': 'Detail view of a specific course',
    'enrollment-list': 'List all enrollments',
    'enrollments-by-student': 'List all enrollments for a specific student',
    'comment-list': 'List all comments',
    'register': 'User registration',
    'login': 'User login',
    'logout': 'User logout',
    'course-create': 'Create a new course',
    'teacher-list': 'List all teachers',
    'user-list': 'List all users'
}

def list_urls(request):
    urlconf = get_resolver()
    urls = urlconf.reverse_dict.keys()
    scheme = request.scheme
    host = request.get_host()
    base_url = f"{scheme}://{host}/"
    
    response = '<h1>Available URLs</h1><ul>'
    for url in urls:
        if url == 'list_urls' or url == 'activate':
            continue
        if isinstance(url, str):  
            try:
                url_path = reverse(url)
                full_url = base_url + url_path.lstrip('/')
                description = url_descriptions.get(url, 'No description available')
                response += format_html('<li><a href="{}">{}</a> - {}</li>', full_url, url, description)
            except Exception as e:
                response += format_html('<li>{} (URL requires parameters) - {}</li>', url, description)
    response += '</ul>'
    return HttpResponse(response)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('departments.urls')),
    path('api/', include('enrollments.urls')),
    path('api/', include('comments.urls')),
    path('api/', include('courses.urls')),
    path('', list_urls, name='list_urls'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
