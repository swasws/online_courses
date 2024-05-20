from django.urls import path
from .views import all_courses_view, my_courses_view, create_course_view, course_detail_view, enroll_course_view

urlpatterns = [
    path('all/', all_courses_view, name='all_courses'),
    path('my/', my_courses_view, name='my_courses'),
    path('create/', create_course_view, name='create_course'),
    path('<int:pk>/', course_detail_view, name='course_detail'),
    path('<int:pk>/enroll/', enroll_course_view, name='enroll_course'),
]
