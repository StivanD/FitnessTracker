# Generated by Django 5.0.4 on 2024-11-29 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_workout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='workout_overview',
        ),
        migrations.AddField(
            model_name='workout',
            name='calories_burned',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='workout',
            name='difficulty',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default='Beginner', max_length=12),
        ),
        migrations.AddField(
            model_name='workout',
            name='duration',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='workout',
            name='equipment_needed',
            field=models.TextField(blank=True, help_text='Details about the needed equipment', null=True),
        ),
    ]
