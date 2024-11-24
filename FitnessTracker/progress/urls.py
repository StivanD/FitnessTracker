from django.urls import path

from FitnessTracker.progress.views import ProgressPageView, LogProgressView, LogHistoryView, LogExerciseView

urlpatterns = [
    path('', ProgressPageView.as_view(), name='progress-page'),
    path('log-progress/', LogProgressView.as_view(), name='log-progress'),
    path('log-history/', LogHistoryView.as_view(), name='log-history'),
    path('log-exercise/', LogExerciseView.as_view(), name='log-exercise')
]