# Generated by Django 5.1.2 on 2024-11-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_espacios', '0006_alter_espaciopublico_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='espaciopublico',
            name='espacio_especial',
            field=models.BooleanField(default=False),
        ),
    ]
