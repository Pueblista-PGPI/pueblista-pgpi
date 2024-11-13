# Generated by Django 5.1.2 on 2024-11-11 17:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_espacios', '0003_alter_espaciopublico_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espaciopublico',
            name='telefono',
            field=models.CharField(max_length=9, validators=[django.core.validators.RegexValidator(message="El número de teléfono debe\n                       ingresarse en el formato: '999999999'.", regex='^\\d{9}$')]),
        ),
    ]