# Generated by Django 3.1.14 on 2022-07-13 14:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0026_auto_20220630_1913"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="payment_method",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="stores.paymentmethod",
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="shipping_method",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="orders",
                to="stores.shippingmethod",
            ),
        ),
    ]
