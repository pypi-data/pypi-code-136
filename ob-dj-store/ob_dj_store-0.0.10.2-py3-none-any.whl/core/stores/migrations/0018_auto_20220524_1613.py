# Generated by Django 3.1.14 on 2022-05-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0017_auto_20220524_0912"),
    ]

    operations = [
        migrations.RenameField(
            model_name="orderitem",
            old_name="variant",
            new_name="product_variant",
        ),
        migrations.AddField(
            model_name="productvariant",
            name="has_inventory",
            field=models.BooleanField(default=True),
        ),
    ]
