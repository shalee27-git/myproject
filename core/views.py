from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.tasks import send_welcome_email
from rest_framework import status
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.
class PublicAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({'message': 'Public Access'})
    
class ProtectedAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message': 'Protected Access'})
    

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = User.objects.create_user(username=username, email=email, password=password)

        send_welcome_email.delay(user.email)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

def home(request):
    return HttpResponse('Welcome to the Home Page!')