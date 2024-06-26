# Generated by Django 4.2.3 on 2023-08-25 08:36

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("telemetry", "0016_landmark_from_cc"),
    ]

    operations = [
        migrations.CreateModel(
            name="TrackGuide",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("description", models.TextField(default="")),
                ("car", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="telemetry.car")),
                ("track", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="telemetry.track")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="TrackGuideNote",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now, editable=False, verbose_name="modified"
                    ),
                ),
                ("segment", models.IntegerField(default=0)),
                ("priority", models.IntegerField(default=0)),
                ("ref_id", models.CharField(default="", max_length=64)),
                ("ref_eval", models.CharField(default="", max_length=64)),
                ("message", models.TextField(default="")),
                ("eval", models.TextField(default="")),
                ("notes", models.TextField(default="")),
                (
                    "landmark",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="notes",
                        to="telemetry.landmark",
                    ),
                ),
                (
                    "track_guide",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="notes", to="telemetry.trackguide"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
