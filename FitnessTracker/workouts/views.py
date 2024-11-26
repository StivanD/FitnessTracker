from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class WorkoutsView(TemplateView):
    template_name = 'workouts/workouts.html'


class WorkoutsDashboardView(TemplateView):
    template_name = 'workouts/workouts-dashboard.html'


class WorkoutDetailsView(TemplateView):
    template_name = 'workouts/workout-details.html'


class CreateWorkoutView(TemplateView):
    template_name = 'workouts/create-workout.html'


class EditWorkoutView(TemplateView):
    template_name = 'workouts/edit-workout.html'


class DeleteWorkoutView(TemplateView):
    template_name = 'workouts/delete-workout.html'


class UserWorkoutsView(TemplateView):
    template_name = 'workouts/user-workouts.html'
