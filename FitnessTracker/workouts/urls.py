from django.urls import path

from FitnessTracker.workouts.views import WorkoutsView, WorkoutsDashboardView, WorkoutDetailsView, EditWorkoutView

urlpatterns = [
    path('', WorkoutsView.as_view(), name='workouts'),
    path('dashboard/', WorkoutsDashboardView.as_view(), name='workouts-dashboard'),
    path('details/', WorkoutDetailsView.as_view(), name='workout-details'),
    path('edit/', EditWorkoutView.as_view(), name='edit-workout')
]