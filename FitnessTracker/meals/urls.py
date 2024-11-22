from django.urls import path

from FitnessTracker.meals.views import MealsDashboardView, AddMealView, EditMealView, RemoveMealView

urlpatterns = [
    path('dashboard/', MealsDashboardView.as_view(), name='meals-dashboard'),
    path('add/', AddMealView.as_view(), name='add-meal'),
    path('edit/', EditMealView.as_view(), name='edit-meal'),
    path('remove/', RemoveMealView.as_view(), name='remove-meal')
]