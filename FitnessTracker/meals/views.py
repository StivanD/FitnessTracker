from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from FitnessTracker.meals.forms import MealCreateForm, MealEditForm
from FitnessTracker.meals.models import Meal


# Create your views here.
class MealsDashboardView(LoginRequiredMixin, ListView):
    model = Meal
    template_name = 'meals/meals-dashboard.html'


class MealCreateView(LoginRequiredMixin, CreateView):
    model = Meal
    form_class = MealCreateForm
    template_name = 'meals/add-meal.html'
    success_url = reverse_lazy('meals-dashboard')

    def form_valid(self, form):
        return super().form_valid(form)


class MealEditView(LoginRequiredMixin, UpdateView):
    model = Meal
    form_class = MealEditForm
    template_name = 'meals/edit-meal.html'
    success_url = reverse_lazy('meals-dashboard')


class MealDeleteView(LoginRequiredMixin, DeleteView):
    model = Meal
    template_name = 'meals/remove-meal.html'
    success_url = reverse_lazy('meals-dashboard')
