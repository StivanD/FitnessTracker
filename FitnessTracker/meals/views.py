from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from FitnessTracker.meals.forms import MealCreateForm, MealEditForm
from FitnessTracker.meals.models import Meal


# Create your views here.
class MealsDashboardView(LoginRequiredMixin, ListView):
    model = Meal
    template_name = 'meals/meals-dashboard.html'

    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)


class MealCreateView(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = MealCreateForm
    template_name = 'meals/add-meal.html'
    success_url = reverse_lazy('meals-dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MealEditView(LoginRequiredMixin, UpdateView):
    model = Meal
    form_class = MealEditForm
    template_name = 'meals/edit-meal.html'
    success_url = reverse_lazy('meals-dashboard')

    def dispatch(self, request, *args, **kwargs):
        meal = get_object_or_404(Meal, pk=self.kwargs['pk'])

        if meal.user != request.user:
            return HttpResponseRedirect(reverse('homepage'))

        return super().dispatch(request, *args, **kwargs)


class MealDeleteView(LoginRequiredMixin, DeleteView):
    model = Meal
    template_name = 'meals/remove-meal.html'
    success_url = reverse_lazy('meals-dashboard')

    def dispatch(self, request, *args, **kwargs):
        meal = get_object_or_404(Meal, pk=self.kwargs['pk'])

        if meal.user != request.user:
            return HttpResponseRedirect(reverse('homepage'))

        return super().dispatch(request, *args, **kwargs)
