from django import forms
from django.forms import TextInput, NumberInput, Textarea

from FitnessTracker.meals.models import Meal


class MealBaseForm(forms.ModelForm):
    class Meta:
        model = Meal
        exclude = ('created_at', 'updated_at')

        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Enter meal name'
                }
            ),
            'calories': NumberInput(
                attrs={
                    'placeholder': 'Enter calorie count'
                }
            ),
            'ingredients': Textarea(
                attrs={
                    'placeholder': 'Enter the ingredients. Ex: ing1, ing2, ing3...',
                    'rows': 3
                }
            ),
            'additional_notes': Textarea(
                attrs={
                    'placeholder': 'Add any notes or comments about the meal',
                    'rows': 3
                }
            )
        }

        labels = {
            'name': 'Meal Name',
            'calories': 'Calories (kcal)',
            'ingredients': 'Ingredients',
            'additional_notes': 'Additional Notes (Optional)'
        }


class MealCreateForm(MealBaseForm):
    pass


class MealEditForm(MealBaseForm):
    pass

