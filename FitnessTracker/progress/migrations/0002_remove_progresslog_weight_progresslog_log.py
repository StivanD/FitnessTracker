# Generated by Django 5.0.4 on 2024-12-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('progress', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progresslog',
            name='weight',
        ),
        migrations.AddField(
            model_name='progresslog',
            name='log',
            field=models.CharField(default='No log', max_length=255),
        ),
    ]