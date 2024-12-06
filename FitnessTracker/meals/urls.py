from django.urls import path, include

from FitnessTracker.meals.views import MealsDashboardView, MealCreateView, MealEditView, MealDeleteView

urlpatterns = [
    path('dashboard/', MealsDashboardView.as_view(), name='meals-dashboard'),
    path('create/', MealCreateView.as_view(), name='create-meal'),
    path('<int:pk>/', include([
        path('edit/', MealEditView.as_view(), name='edit-meal'),
        path('remove/', MealDeleteView.as_view(), name='remove-meal')
    ])),
]
