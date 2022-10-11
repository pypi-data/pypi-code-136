# Generated by Django 3.2.3 on 2021-07-22 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='unit',
            new_name='category',
        ),
        migrations.AlterUniqueTogether(
            name='measurement',
            unique_together={('date', 'category')},
        ),
        migrations.RemoveField(
            model_name='measurement',
            name='user',
        ),
    ]
