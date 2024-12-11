from django.contrib import admin
from .models import Workout, WorkoutCategory, FavouriteWorkouts


@admin.register(WorkoutCategory)
class WorkoutCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'to_be_displayed')
    search_fields = ('name', 'description')
    list_filter = ('to_be_displayed',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'duration', 'calories_burned', 'creator', 'created_at', 'visit_count')
    search_fields = ('name', 'short_description', 'creator__email', 'creator__username')
    list_filter = ('difficulty', 'created_at', 'category')
    ordering = ('-created_at',)


@admin.register(FavouriteWorkouts)
class FavouriteWorkoutsAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__email', 'user__username')
    filter_horizontal = ('workouts',)
