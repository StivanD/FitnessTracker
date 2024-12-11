# Generated by Django 5.0.4 on 2024-12-11 10:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_appuser_first_name_alter_appuser_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(2, 'The username must contain at least 2 symbols!')]),
        ),
    ]