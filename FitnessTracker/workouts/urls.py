from django.urls import path

from FitnessTracker.workouts.views import WorkoutsView, WorkoutsDashboardView, WorkoutDetailsView, EditWorkoutView, \
    CreateWorkoutView, DeleteWorkoutView, UserWorkoutsView, UserFavouriteWorkoutsView

urlpatterns = [
    path('', WorkoutsView.as_view(), name='workouts'),
    path('dashboard/', WorkoutsDashboardView.as_view(), name='workouts-dashboard'),
    path('details/<int:pk>/', WorkoutDetailsView.as_view(), name='workout-details'),
    path('create/', CreateWorkoutView.as_view(), name='create-workout'),
    path('edit/', EditWorkoutView.as_view(), name='edit-workout'),
    path('delete/', DeleteWorkoutView.as_view(), name='delete-workout'),
    path('user-workouts/', UserWorkoutsView.as_view(), name='user-workouts'),
    path('favourite-workouts', UserFavouriteWorkoutsView.as_view(), name='favourite-workouts')
]