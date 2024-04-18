# Generated by Django 4.2.11 on 2024-04-17 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("dbcore", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Database",
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
                ("title", models.CharField(max_length=256)),
                ("description", models.CharField(max_length=256)),
                ("server_id", models.IntegerField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Types",
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
                ("title", models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name="element",
            name="type",
        ),
        migrations.DeleteModel(
            name="DBTypes",
        ),
        migrations.DeleteModel(
            name="Element",
        ),
        migrations.AddField(
            model_name="database",
            name="type_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="dbcore.types"
            ),
        ),
    ]
