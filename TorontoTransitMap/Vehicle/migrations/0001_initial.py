# Generated by Django 5.0 on 2024-01-02 18:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Company", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vehicle",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model", models.CharField(blank=True, max_length=255)),
                ("year", models.PositiveIntegerField(blank=True)),
                (
                    "vehicle_type",
                    models.IntegerField(
                        choices=[
                            (0, "Streetcar"),
                            (1, "Subway"),
                            (2, "RT"),
                            (3, "Bus"),
                            (4, "Unknown"),
                        ],
                        default=4,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Company.company",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
