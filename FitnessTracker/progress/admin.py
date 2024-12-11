from django.contrib import admin
from .models import ProgressExercise, ProgressLog


@admin.register(ProgressExercise)
class ProgressExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')
    search_fields = ('name', 'user__email', 'user__username')


@admin.register(ProgressLog)
class ProgressLogAdmin(admin.ModelAdmin):
    list_display = ('exercise', 'log', 'date')
    search_fields = ('exercise__name', 'log')
    list_filter = ('date',)
    ordering = ('-date',)
