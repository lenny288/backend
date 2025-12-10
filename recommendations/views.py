from django.shortcuts import render

# Create your views here.

<<<<<<< HEAD
rom rest_framework.views import APIView
=======
from rest_framework.views import APIView
>>>>>>> ba7a5b5 (commit all changes mad)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from workouts.models import Workout
from collections import Counter

class RecommendationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        workouts = Workout.objects.filter(user=user)
        
        if not workouts.exists():
            # If no history, recommend some default workouts
            suggestions = [
                {"title": "Morning Run", "duration": 30, "calories_burned": 250},
                {"title": "Yoga Stretch", "duration": 20, "calories_burned": 100}
            ]
        else:
            # Recommend based on most frequent workouts
            titles = [w.title for w in workouts]
            most_common = Counter(titles).most_common(2)
            suggestions = []
            for title, _ in most_common:
                similar = workouts.filter(title=title).first()
                suggestions.append({
                    "title": similar.title,
                    "duration": similar.duration,
                    "calories_burned": similar.calories_burned
                })
        
        return Response({"recommendations": suggestions})
