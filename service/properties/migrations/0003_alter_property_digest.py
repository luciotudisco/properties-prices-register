# Generated by Django 5.0.1 on 2024-01-09 20:35
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("properties", "0002_remove_property_google_place_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="digest",
            field=models.CharField(max_length=32),
        ),
    ]
