# Generated by Django 5.1.2 on 2024-11-18 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_espacios', '0006_alter_espaciopublico_estado'),
        ('gestion_reservas', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reserva',
            unique_together={('espacio', 'fecha', 'hora_inicio')},
        ),
    ]
