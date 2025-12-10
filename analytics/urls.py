

from django.urls import path
from .views import WeeklyAnalyticsView

urlpatterns = [
    path('weekly/', WeeklyAnalyticsView.as_view(), name='weekly-analytics'),
]



from django.urls import path
from .views import WeeklyAnalyticsView

urlpatterns = [
    path('weekly/', WeeklyAnalyticsView.as_view(), name='weekly-analytics'),
]

