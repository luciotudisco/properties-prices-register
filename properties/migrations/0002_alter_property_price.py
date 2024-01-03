# Generated by Django 5.0.1 on 2024-01-03 22:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("properties", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=20, null=True
            ),
        ),
    ]
