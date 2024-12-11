from django.contrib import admin
from .models import Meal


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'created_at', 'updated_at')
    search_fields = ('name', 'ingredients', 'additional_notes')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
