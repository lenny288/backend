<<<<<<< HEAD
from django.urls import path
from .views import RecommendationView

urlpatterns = [
    path('', RecommendationView.as_view(), name='recommendations'),
]
=======

from django.urls import path
from .views import RecommendationView

urlpatterns = [
    path('', RecommendationView.as_view(), name='recommendations'),
]
>>>>>>> ba7a5b5 (commit all changes mad)
