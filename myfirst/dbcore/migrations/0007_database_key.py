# Generated by Django 4.2.11 on 2024-04-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbcore', '0006_remove_server_type_delete_database_server_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='key',
            field=models.CharField(default='L617Ggzw', max_length=256),
        ),
    ]
