# Generated by Django 5.1.2 on 2024-11-22 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_espacios', '0009_espaciopublico_subespacios'),
        ('gestion_reservas', '0007_reserva_nombre'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reserva',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='reserva',
            name='subespacio',
            field=models.CharField(default='No procede', max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='reserva',
            unique_together={('espacio', 'subespacio', 'fecha', 'hora_inicio')},
        ),
    ]
