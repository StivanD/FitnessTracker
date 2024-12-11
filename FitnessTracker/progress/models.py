from django.conf import settings
from django.db import models

import FitnessTracker.accounts.models


# Create your models here.
class ProgressExercise(models.Model):
    name = models.CharField(
        max_length=255
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='progress_exercises'
    )

    def __str__(self):
        return f"{self.name}"


class ProgressLog(models.Model):
    class Meta:
        ordering = ['-date']

    exercise = models.ForeignKey(
        to=ProgressExercise,
        on_delete=models.CASCADE,
        related_name='progress_logs'
    )

    log = models.CharField(
        max_length=255,
        blank=True
    )

    date = models.DateField()

    def __str__(self):
        return f"{self.log} on {self.date}"
