from django.db import models
from django.shortcuts import redirect, render
from django.core.validators import RegexValidator


class EspacioPublico(models.Model):
    RESERVADO = "reservado"
    LIBRE = "libre"
    NO_DISPONIBLE = "no_disponible"

    ESTADO = [
        (RESERVADO, 'Reservado'),
        (LIBRE, 'Libre'),
        (NO_DISPONIBLE, 'No Disponible'),
    ]

    nombre = models.CharField(max_length=100, null=False, blank=False)
    horario = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    fotos = models.ImageField(upload_to='spaces',
                              verbose_name='photo', null=True, blank=True)
    telefono = models.CharField(max_length=9, validators=[
        RegexValidator(regex=r'^\d{9}$',
                       message='''El número de teléfono debe
                       ingresarse en el formato: '999999999'.''')],
                                null=False, blank=False)
    estado = models.CharField(max_length=15, choices=ESTADO, default=LIBRE)

    def __str__(self):
        return self.nombre

    REQUIRED_FIELDS = ['nombre', 'horario', 'descripcion',
                       'telefono', 'estado']

    def editar_espacio(self, nombre=None, horario=None, descripcion=None,
                       fotos=None, estado=None, telefono_atencion=None):
        if nombre:
            self.nombre = nombre
        if horario:
            self.horario = horario
        if descripcion:
            self.descripcion = descripcion
        if fotos:
            self.fotos = fotos
        if estado:
            self.estado = estado
        if telefono_atencion:
            self.telefono_atencion = telefono_atencion
        self.save()
        return self

    def borrar_espacio(self):
        self.delete()
