# Generated by Django 4.2.11 on 2024-04-18 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dbcore", "0003_ports_server_type_server_database_server"),
    ]

    operations = [
        migrations.AlterField(
            model_name="database",
            name="server_id",
            field=models.IntegerField(),
        ),
    ]
