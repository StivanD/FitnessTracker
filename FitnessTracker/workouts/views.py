from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class WorkoutsView(TemplateView):
    template_name = 'workouts/workouts.html'


class WorkoutsDashboardView(TemplateView):
    template_name = 'workouts/workouts-dashboard.html'


class WorkoutDetailsView(TemplateView):
    template_name = 'workouts/workout-details.html'
