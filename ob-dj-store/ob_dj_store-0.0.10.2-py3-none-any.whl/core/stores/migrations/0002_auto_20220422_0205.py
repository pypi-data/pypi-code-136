# Generated by Django 3.1.14 on 2022-04-21 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="store",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
