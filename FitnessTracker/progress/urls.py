from django.urls import path, include

from FitnessTracker.progress.views import ProgressPageView, LogProgressView, LogHistoryView, LogExerciseView, \
    LogEditView, LogDeleteView

urlpatterns = [
    path('', ProgressPageView.as_view(), name='progress-page'),
    path('log-exercise/', LogExerciseView.as_view(), name='log-exercise'),
    path('<int:exercise_id>/', include([
        path('log/', LogProgressView.as_view(), name='log-progress'),
        path('history', LogHistoryView.as_view(), name='log-history')
    ])),
    path('<int:pk>/', include([
        path('edit/', LogEditView.as_view(), name='log-edit'),
        path('url/', LogDeleteView.as_view(), name='log-delete')
    ]))
]
