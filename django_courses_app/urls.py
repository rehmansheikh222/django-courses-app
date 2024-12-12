"""
URLs for django_courses_app.
"""
from django.urls import path  # pylint: disable=unused-import
from .views import CourseOverviewList, CourseEnrollmentAPIView

urlpatterns = [
    path('courses/', CourseOverviewList.as_view(), name='django-courses-list'),
    path(
        'enrollments/', CourseEnrollmentAPIView.as_view(), name='django-courses-enrollments'
    ),
]
