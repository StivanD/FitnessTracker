from django.conf import settings
from django.db import models


# Create your models here.
class Meal(models.Model):
    class Meta:
        ordering = ['-created_at']

    name = models.CharField(
        max_length=255
    )

    calories = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )

    ingredients = models.TextField(
        null=True,
        blank=True
    )

    additional_notes = models.TextField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='meals',
    )

    def __str__(self):
        return self.name


