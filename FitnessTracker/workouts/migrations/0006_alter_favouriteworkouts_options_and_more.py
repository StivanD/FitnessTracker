# Generated by Django 5.0.4 on 2024-12-11 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0005_favouriteworkouts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favouriteworkouts',
            options={'verbose_name_plural': 'Favourite workouts'},
        ),
        migrations.AlterModelOptions(
            name='workoutcategory',
            options={'verbose_name_plural': 'Workout categories'},
        ),
    ]
