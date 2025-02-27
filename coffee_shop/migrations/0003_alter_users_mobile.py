# Generated by Django 5.1.6 on 2025-02-27 05:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee_shop', '0002_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Mobile number must be exactly 11 digits.', regex='^\\d{11}$')]),
        ),
    ]
