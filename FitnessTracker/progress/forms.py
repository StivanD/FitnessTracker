from django import forms
from django.forms import TextInput, DateInput

from FitnessTracker.progress.models import ProgressExercise, ProgressLog


class LogExerciseForm(forms.ModelForm):
    class Meta:
        model = ProgressExercise
        fields = ['name']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter exercise name',
                    'required': True,
                }),
        }

        labels = {
            'name': 'Exercise Name',
        }


class LogProgressForm(forms.ModelForm):
    class Meta:
        model = ProgressLog
        fields = ['log', 'date']

        widgets = {
            'log': TextInput(
                attrs={
                    'placeholder': 'Ex: 120kg for 5 reps / 15 seconds static hold etc...',
                    'required': True
                }
            ),
            'date': DateInput(
                attrs={
                    'type': 'date',
                    'required': True
                }
            )
        }

    # Dynamic initialization to link the log with a specific exercise
    def __init__(self, *args, **kwargs):
        self.exercise = kwargs.pop('exercise', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.exercise:
            instance.exercise = self.exercise
        if commit:
            instance.save()
        return instance
