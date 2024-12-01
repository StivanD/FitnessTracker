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
            'short_description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'A brief description of the workout'}),
            'workout_breakdown': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe workout phases'}),
            'exercise_list': forms.Textarea(attrs={'rows': 4, 'placeholder': 'List exercises with sets/reps'}),
            'creator_tips': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Provide tips about form and mistakes'}),
            'benefits': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Highlight workout benefits'}),
            'expectations': forms.Textarea(attrs={'rows': 4, 'placeholder': 'What to expect after completion'}),
            'equipment_needed': forms.Textarea(attrs={'rows': 2, 'placeholder': 'E.g., Dumbbells, Resistance Bands'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'difficulty': forms.Select(attrs={'class': 'form-select'}),
        }


class EditWorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'category', 'short_description', 'duration', 'difficulty', 'equipment_needed',
                  'calories_burned', 'workout_breakdown', 'exercise_list', 'creator_tips', 'benefits', 'expectations',
                  'image']
