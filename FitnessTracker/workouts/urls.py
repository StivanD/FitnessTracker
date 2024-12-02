from django.urls import path, include

from FitnessTracker.workouts.views import WorkoutsView, WorkoutsDashboardView, WorkoutDetailsView, EditWorkoutView, \
    CreateWorkoutView, DeleteWorkoutView, UserWorkoutsListView, UserFavouriteWorkoutsView

urlpatterns = [
    path('', WorkoutsView.as_view(), name='workouts'),
    path('dashboard/', WorkoutsDashboardView.as_view(), name='workouts-dashboard'),
    path('<int:pk>/', include([
        path('details/', WorkoutDetailsView.as_view(), name='workout-details'),
        path('edit/', EditWorkoutView.as_view(), name='edit-workout'),
        path('delete/', DeleteWorkoutView.as_view(), name='delete-workout'),
    ])),
    path('create/', CreateWorkoutView.as_view(), name='create-workout'),
    path('user-workouts/<str:username>/', UserWorkoutsListView.as_view(), name='user-workouts'),
    path('favourite-workouts', UserFavouriteWorkoutsView.as_view(), name='favourite-workouts')
]
