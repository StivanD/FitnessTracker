# forms.py
from django import forms
from .models import Workout, WorkoutCategory


class CreateWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = [
            'name',
            'short_description',
            'duration',
            'difficulty',
            'equipment_needed',
            'calories_burned',
            'workout_breakdown',
            'exercise_list',
            'creator_tips',
            'benefits',
            'expectations',
            'category',
            'image',
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the workout\'s name'
                }
            ),
            'category': forms.Select(
                attrs={
                    'placeholder': 'Select category'
                }
            ),
            'short_description': forms.Textarea(
                attrs={
                    'placeholder': 'A brief description of the workout',
                    'rows': 3
                }
            ),
            'duration': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter duration in minutes'}
            ),
            'difficulty': forms.Select(
                attrs={
                    'placeholder': 'Select difficulty level'
                }
            ),
            'equipment_needed': forms.Textarea(
                attrs={
                    'placeholder': 'E.g., Dumbbells, Resistance Bands',
                    'rows': 2
                }
            ),
            'calories_burned': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter estimated calories burned'
                }
            ),
            'workout_breakdown': forms.Textarea(
                attrs={
                    'placeholder': 'Describe workout phases',
                    'rows': 4
                }
            ),
            'exercise_list': forms.Textarea(
                attrs={
                    'placeholder': 'List exercises with sets/reps',
                    'rows': 4
                }
            ),
            'creator_tips': forms.Textarea(
                attrs={
                    'placeholder': 'Provide tips about form and mistakes',
                    'rows': 3
                }
            ),
            'benefits': forms.Textarea(
                attrs={
                    'placeholder': 'Highlight workout benefits',
                    'rows': 4
                }
            ),
            'expectations': forms.Textarea(
                attrs={
                    'placeholder': 'What to expect after completion',
                    'rows': 4
                }
            )
        }


class EditWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'category', 'short_description', 'duration', 'difficulty', 'equipment_needed',
                  'calories_burned', 'workout_breakdown', 'exercise_list', 'creator_tips', 'benefits', 'expectations',
                  'image']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter the workout\'s name'
                }
            ),
            'category': forms.Select(
                attrs={
                    'placeholder': 'Select category'
                }
            ),
            'short_description': forms.Textarea(
                attrs={
                    'placeholder': 'A brief description of the workout',
                    'rows': 3
                }
            ),
            'duration': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter duration in minutes'}
            ),
            'difficulty': forms.Select(
                attrs={
                    'placeholder': 'Select difficulty level'
                }
            ),
            'equipment_needed': forms.Textarea(
                attrs={
                    'placeholder': 'E.g., Dumbbells, Resistance Bands',
                    'rows': 2
                }
            ),
            'calories_burned': forms.NumberInput(
                attrs={
                    'placeholder': 'Enter estimated calories burned'
                }
            ),
            'workout_breakdown': forms.Textarea(
                attrs={
                    'placeholder': 'Describe workout phases',
                    'rows': 4
                }
            ),
            'exercise_list': forms.Textarea(
                attrs={
                    'placeholder': 'List exercises with sets/reps',
                    'rows': 4
                }
            ),
            'creator_tips': forms.Textarea(
                attrs={
                    'placeholder': 'Provide tips about form and mistakes',
                    'rows': 3
                }
            ),
            'benefits': forms.Textarea(
                attrs={
                    'placeholder': 'Highlight workout benefits',
                    'rows': 4
                }
            ),
            'expectations': forms.Textarea(
                attrs={
                    'placeholder': 'What to expect after completion',
                    'rows': 4
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'placeholder': 'Upload a new workout image',
                }
            )
        }

        labels = {
            'name': 'Workout Name',
            'category': 'Category',
            'short_description': 'Description',
            'duration': 'Duration (minutes)',
            'difficulty': 'Difficulty',
            'equipment_needed': 'Equipment Needed',
            'calories_burned': 'Calories Burned (kcal)',
            'workout_breakdown': 'Workout Breakdown',
            'exercise_list': 'Detailed Exercise List',
            'creator_tips': 'Creator Tips',
            'benefits': 'Benefits',
            'expectations': 'What to Expect',
            'image': 'Change Workout Image',
        }
