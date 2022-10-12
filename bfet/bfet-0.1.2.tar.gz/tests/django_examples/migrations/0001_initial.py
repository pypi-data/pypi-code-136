from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="FKTestingModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("name", models.CharField(max_length=32, unique=True)),
                ("non_filled", models.CharField(max_length=32)),
            ],
            options={
                "verbose_name": "FKTestingModel",
                "db_table": "django_examples_fktestingmodel",
            },
        ),
    ]
