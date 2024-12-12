from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from openedx.core.djangoapps.content.course_overviews.serializers import CourseOverviewBaseSerializer
from rest_framework.permissions import IsAuthenticated
from openedx.core.lib.api.authentication import BearerAuthentication


class CourseEnrollmentAPIView(APIView):
    """
    API view to return dummy course enrollment data.
    """
    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        dummy_data = [
            {"course_id": "course_101", "enrollments": 250},
            {"course_id": "course_102", "enrollments": 180},
        ]
        return Response(dummy_data, status=200)


class CourseOverviewList(APIView):
    """
    API view to retrieve list of courses with optional filtering by title and language.
    """

    def get(self, request, format=None):
        """
        Return a list of courses, optionally filtered by title and/or language.
        """
        title = request.query_params.get('title', None)
        language = request.query_params.get('language', None)

        courses = CourseOverview.objects.all()

        if title:
            courses = courses.filter(display_name__icontains=title)
        if language:
            courses = courses.filter(language__iexact=language)

        serializer = CourseOverviewBaseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
