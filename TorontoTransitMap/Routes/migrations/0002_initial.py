# Generated by Django 5.0 on 2024-01-02 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Routes", "0001_initial"),
        ("Stops", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="route",
            name="trips",
            field=models.ManyToManyField(to="Stops.trip"),
        ),
    ]
