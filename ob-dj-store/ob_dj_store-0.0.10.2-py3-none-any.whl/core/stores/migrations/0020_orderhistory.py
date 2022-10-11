# Generated by Django 3.1.14 on 2022-05-27 15:08

import django.db.models.deletion
from django.db import migrations, models

import ob_dj_store.utils.model


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0019_product_is_featured"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrderHistory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("ACCEPTED", "accepted"),
                            ("CANCELLED", "cancelled"),
                            ("PENDING", "pending"),
                            ("PREPARING", "preparing"),
                            ("READY", "ready for pickup"),
                            ("DELIVERED", "delivered"),
                            ("PAID", "paid"),
                            ("OPENED", "opened"),
                        ],
                        max_length=32,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="history",
                        to="stores.order",
                    ),
                ),
            ],
            options={
                "verbose_name": "Order History",
                "verbose_name_plural": "Order Histories",
            },
            bases=(ob_dj_store.utils.model.DjangoModelCleanMixin, models.Model),
        ),
    ]
