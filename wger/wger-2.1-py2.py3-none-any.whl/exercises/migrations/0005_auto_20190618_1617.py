# -*- coding: utf-8 -*-

# Generated by Django 1.11.21 on 2019-06-18 16:17
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0004_auto_20170404_0114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={
                'base_manager_name': 'objects',
                'ordering': ['name']
            },
        ),
        migrations.AlterModelOptions(
            name='exerciseimage',
            options={
                'base_manager_name': 'objects',
                'ordering': ['-is_main', 'id']
            },
        ),
    ]
