
from rest_framework import serializers
from .models import Workout

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'user', 'title', 'description', 'duration', 'calories_burned', 'date']
        read_only_fields = ['user', 'date']
