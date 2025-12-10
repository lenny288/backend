from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions
from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutListCreateView(generics.ListCreateAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WorkoutDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Workout.objects.filter(user=self.request.user)
