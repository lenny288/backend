from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"})
        except Exception:
            return Response({"error": "Invalid token"}, status=400)
