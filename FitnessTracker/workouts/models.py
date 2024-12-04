from django.contrib.auth import get_user_model
from django.db import models

from FitnessTracker.workouts.choices import WorkoutDifficultyLevels

User = get_user_model()


# Create your models here.
class WorkoutCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to='category_images/'
    )

    to_be_displayed = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )

    short_description = models.TextField()

    duration = models.PositiveIntegerField(
        default=0
    )

    difficulty = models.CharField(
        max_length=12,
        choices=WorkoutDifficultyLevels.choices,
        default=WorkoutDifficultyLevels.BEGINNER
    )

    equipment_needed = models.TextField(
        help_text="Details about the needed equipment",
        null=True,
        blank=True
    )

    calories_burned = models.PositiveIntegerField(
        default=0
    )

    workout_breakdown = models.TextField(
        help_text="Details about the phases of the workout."
    )

    exercise_list = models.TextField(
        help_text="List of exercises with sets, reps, and descriptions."
    )

    creator_tips = models.TextField(
        help_text="Tips from the creator about form and common mistakes."
    )

    benefits = models.TextField(
        help_text="Benefits users can expect from this workout."
    )

    expectations = models.TextField(
        help_text="What users can expect after completing the workout."
    )

    creator = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="workouts"
    )

    visit_count = models.PositiveIntegerField(
        default=0
    )

    category = models.ForeignKey(
        to="WorkoutCategory",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    image = models.ImageField(
        upload_to="workouts/",
        null=True,
        blank=True,
        default="default_images/default-workout-image.jpg"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FavouriteWorkouts(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='favourites'
    )

    workouts = models.ManyToManyField(
        Workout,
        blank=True,
        related_name='favourited_by'
    )

    def __str__(self):
        return f"{self.user.username}'s Favourites"
