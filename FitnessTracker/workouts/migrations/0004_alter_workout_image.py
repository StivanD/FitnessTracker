# Generated by Django 5.0.4 on 2024-12-01 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_remove_workout_workout_overview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='image',
            field=models.ImageField(blank=True, default='default_images/default-workout-image.jpg', null=True, upload_to='workouts/'),
        ),
    ]
