from django.db import models


class WorkoutDifficultyLevels(models.TextChoices):
    BEGINNER = 'Beginner', 'Beginner'
    INTERMEDIATE = 'Intermediate', 'Intermediate'
    ADVANCED = 'Advanced', 'Advanced'
