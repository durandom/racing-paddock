# Generated by Django 5.1b1 on 2024-11-12 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("telemetry", "0032_alter_car_unique_together"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="car",
            unique_together={("game", "name", "car_class")},
        ),
    ]
