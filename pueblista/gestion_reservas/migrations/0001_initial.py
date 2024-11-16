
from django.db import models, migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ]

    operations = [
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True, primary_key=True,
                    serialize=False, verbose_name='ID')),

                ('fecha', models.DateField()),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('estado', models.CharField(
                    choices=[('Realizada', 'Realizada'),
                             ('Cancelada', 'Cancelada'),
                             ('En curso', 'En curso'),
                             ('Finalizada', 'Finalizada')],
                    default='Realizada', max_length=30)),

                ('espacio', models.ForeignKey(
                    on_delete=models.CASCADE,
                    to='gestion_espacios.EspacioPublico')),

                ('usuario', models.ForeignKey(
                    on_delete=models.CASCADE,
                    to='gestion_usuarios.CustomUser')),

            ],
        ),
    ]
