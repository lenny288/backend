from django.db import models

# Create your models here.

from django.db import models
from django.conf import settings

class Workout(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    calories_burned = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.user.username}"
