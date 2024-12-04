from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView, DeleteView

from FitnessTracker.workouts.forms import CreateWorkoutForm, EditWorkoutForm
from FitnessTracker.workouts.models import WorkoutCategory, Workout, User, FavouriteWorkouts


# Create your views here.
class WorkoutsView(TemplateView):
    template_name = "workouts/workouts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch categories
        context['categories'] = WorkoutCategory.objects.all()

        # Fetch featured workouts (top 3 most visited)
        context['featured_workouts'] = Workout.objects.order_by('-visit_count')[:3]

        # Fetch favourite workouts for the logged-in user
        if self.request.user.is_authenticated:
            user_favourites = FavouriteWorkouts.objects.filter(user=self.request.user).first()
            context['favourite_workouts'] = user_favourites.workouts.all() if user_favourites else []
        else:
            context['favourite_workouts'] = []

        return context


class WorkoutsDashboardView(ListView):
    model = Workout
    template_name = "workouts/workouts-dashboard.html"
    context_object_name = "workouts"

    def get_queryset(self):
        return Workout.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = WorkoutCategory.objects.all()

        # Fetch favourite workouts for the logged-in user
        if self.request.user.is_authenticated:
            user_favourites = FavouriteWorkouts.objects.filter(user=self.request.user).first()
            context['favourite_workouts'] = user_favourites.workouts.all() if user_favourites else []
        else:
            context['favourite_workouts'] = []

        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user_favourites = FavouriteWorkouts.objects.filter(user=self.request.user).first()
        context['favourite_workouts'] = user_favourites.workouts.all() if user_favourites else []

        return context


class CreateWorkoutView(CreateView):
    model = CreateWorkoutForm
    template_name = 'workouts/create-workout.html'
    form_class = CreateWorkoutForm

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('user-workouts', kwargs={'username': self.request.user.username})


class EditWorkoutView(UpdateView):
    model = Workout
    form_class = EditWorkoutForm
    template_name = 'workouts/edit-workout.html'
    context_object_name = 'workout'

    def get_success_url(self):
        return reverse_lazy('workout-details', kwargs={'pk': self.object.pk})

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)

    def form_valid(self, form):
        if 'image-clear' in self.request.POST:
            form.instance.image = "default_images/default-workout-image.jpg"

        return super().form_valid(form)


class DeleteWorkoutView(DeleteView):
    model = Workout
    template_name = 'workouts/delete-workout.html'
    context_object_name = 'workout'

    def get_queryset(self):
        return super().get_queryset().filter(creator=self.request.user)

    def get_success_url(self):
        return reverse('user-workouts', kwargs={'username': self.request.user.username})


class UserWorkoutsListView(ListView):
    model = Workout
    template_name = 'workouts/user-workouts.html'
    context_object_name = 'workouts'

    def get_queryset(self):
        # Filter workouts by the specified username
        username = self.kwargs.get('username')
        self.profile_user = get_object_or_404(User, username=username)
        return Workout.objects.filter(creator=self.profile_user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user'] = self.profile_user
        context['is_own_profile'] = self.request.user == self.profile_user
        context['categories'] = WorkoutCategory.objects.all()

        user_favourites = FavouriteWorkouts.objects.filter(user=self.request.user).first()
        context['favourite_workouts'] = user_favourites.workouts.all() if user_favourites else []

        return context


class ToggleFavouriteWorkoutView(View):
    def post(self, request, pk):
        if not request.user.is_authenticated:
            return JsonResponse({'error': 'Unauthorized'}, status=401)

        workout = get_object_or_404(Workout, pk=pk)
        favourite_workouts, created = FavouriteWorkouts.objects.get_or_create(user=request.user)

        # Check if the workout is already in the user's favourites
        if workout in favourite_workouts.workouts.all():
            favourite_workouts.workouts.remove(workout)
            action = 'removed from'
        else:
            favourite_workouts.workouts.add(workout)
            action = 'added to'

        # Return response indicating the action taken
        return JsonResponse({'status': action, 'message': f'Workout {action} favourites.'})


class UserFavouriteWorkoutsView(LoginRequiredMixin, TemplateView):
    template_name = 'workouts/favourite-workouts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_favourites = FavouriteWorkouts.objects.filter(user=self.request.user).first()

        # Simply pass the user's favourite workouts
        context['workouts'] = user_favourites.workouts.all() if user_favourites else []

        context['categories'] = WorkoutCategory.objects.all()
        context['profile_user'] = self.request.user

        return context

