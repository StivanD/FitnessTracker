from django.urls import path
from FitnessTracker.common.views import HomepageView

urlpatterns = [
    path('', HomepageView.as_view(), name='homepage'),
]