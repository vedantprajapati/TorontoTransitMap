# Generated by Django 5.0 on 2024-01-02 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Routes", "0002_initial"),
        ("Vehicle", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="route",
            name="vehicle",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Vehicle.vehicle",
            ),
        ),
    ]
