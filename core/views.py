from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .serializers import UserSerializer
# Create your views here.


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Account successfully created!",
            }, status=status.HTTP_201_CREATED)
        
        return Response(
            {"message": "Make sure you provide valid data"},
            status=status.HTTP_400_BAD_REQUEST
        )
