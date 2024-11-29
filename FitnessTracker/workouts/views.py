from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView

from FitnessTracker.workouts.models import WorkoutCategory, Workout


# Create your views here.
class WorkoutsView(TemplateView):
    template_name = "workouts/workouts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch categories
        context['categories'] = WorkoutCategory.objects.all()

        # Fetch featured workouts (top 3 most visited)
        context['featured_workouts'] = Workout.objects.order_by('-visit_count')[:3]

        return context


class WorkoutsDashboardView(ListView):
    model = Workout
    template_name = "workouts/workouts-dashboard.html"
    context_object_name = "workouts"

    def get_queryset(self):
        return Workout.objects.all()


class WorkoutDetailsView(LoginRequiredMixin, DetailView):
    model = Workout
    template_name = "workouts/workout-details.html"
    context_object_name = "workout"

    def get_object(self, queryset=None):
        workout = super().get_object(queryset)

        if self.request.user.is_authenticated and self.request.user != workout.creator:
            workout.visit_count = workout.visit_count + 1
            workout.save(update_fields=['visit_count'])

        return workout


class CreateWorkoutView(TemplateView):
    template_name = 'workouts/create-workout.html'


class EditWorkoutView(TemplateView):
    template_name = 'workouts/edit-workout.html'


class DeleteWorkoutView(TemplateView):
    template_name = 'workouts/delete-workout.html'


class UserWorkoutsView(TemplateView):
    template_name = 'workouts/user-workouts.html'


class UserFavouriteWorkoutsView(TemplateView):
    template_name = 'workouts/favourite-workouts.html'
