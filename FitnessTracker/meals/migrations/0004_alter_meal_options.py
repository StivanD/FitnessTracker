# Generated by Django 5.0.4 on 2024-12-07 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meals', '0003_alter_meal_ingredients'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['-created_at']},
        ),
    ]