# -*- coding: utf-8 -*-

# Generated by Django 1.11.21 on 2019-06-18 16:17
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='languageconfig',
            name='item',
            field=models.CharField(
                choices=[
                    ('1', 'Exercises'),
                    ('2', 'Ingredients'),
                ], editable=False, max_length=2
            ),
        ),
    ]
