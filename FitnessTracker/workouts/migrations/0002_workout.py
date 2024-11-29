# Generated by Django 5.0.4 on 2024-11-29 14:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('short_description', models.TextField()),
                ('workout_overview', models.TextField(help_text='Store duration, difficulty, equipment, and calories burned.')),
                ('workout_breakdown', models.TextField(help_text='Details about the phases of the workout.')),
                ('exercise_list', models.TextField(help_text='List of exercises with sets, reps, and descriptions.')),
                ('creator_tips', models.TextField(help_text='Tips from the creator about form and common mistakes.')),
                ('benefits', models.TextField(help_text='Benefits users can expect from this workout.')),
                ('expectations', models.TextField(help_text='What users can expect after completing the workout.')),
                ('visit_count', models.PositiveIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='workouts/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workouts.workoutcategory')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
