# Generated by Django 5.1.2 on 2024-11-28 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_delete_configuracion_delete_configuracionadmin'),
    ]

    operations = [
        migrations.AddField(
            model_name='ayuntamientoinfo',
            name='fotos',
            field=models.TextField(blank=True, null=True),
        ),
    ]