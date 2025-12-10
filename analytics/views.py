from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from workouts.models import Workout
from django.db.models import Sum, Avg, Count
from datetime import timedelta

class WeeklyAnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        today = timezone.now().date()
        week_ago = today - timedelta(days=7)

        workouts = Workout.objects.filter(user=user, date__gte=week_ago, date__lte=today)

        total_calories = workouts.aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0
        total_workouts = workouts.count()
        avg_duration = workouts.aggregate(Avg('duration'))['duration__avg'] or 0

        data = {
            "total_calories_burned": total_calories,
            "total_workouts": total_workouts,
            "average_duration": round(avg_duration, 2)
        }
        return Response(data)
