from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Teacher

# from .permissions import TeacherListPermission
from .serializers import TeacherProfileImageSerializer, TeacherSerializer


class TeacherList(APIView):
    def get(self, request):
        q = request.query_params.get("q", "")
        teachers = Teacher.objects.filter(description__icontains=q)
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
