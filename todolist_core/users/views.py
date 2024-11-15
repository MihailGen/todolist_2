from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .models import User
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class CustomView(APIView):
    permission_classes = [IsAuthenticated]
