from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class MealsDashboardView(TemplateView):
    template_name = 'meals/meals-dashboard.html'


class AddMealView(TemplateView):
    template_name = 'meals/add-meal.html'


class EditMealView(TemplateView):
    template_name = 'meals/edit-meal.html'


class RemoveMealView(TemplateView):
    template_name = 'meals/remove-meal.html'
