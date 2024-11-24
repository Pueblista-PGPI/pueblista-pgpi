from django.db import models
from django.core.validators import RegexValidator
import base64


class EspacioPublico(models.Model):
    DISPONIBLE = "disponible"
    NO_DISPONIBLE = "no_disponible"

    ESTADO = [
        (DISPONIBLE, 'Disponible'),
        (NO_DISPONIBLE, 'No Disponible'),
    ]

    nombre = models.CharField(max_length=100, null=False, blank=False)
    horario = models.CharField(max_length=100, null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)
    fotos = models.TextField(null=True, blank=True)
    telefono = models.CharField(max_length=9, validators=[
        RegexValidator(regex=r'^\d{9}$',
                       message='''El número de teléfono debe
                       ingresarse en el formato: '999999999'.''')],
                                null=False, blank=False)
    estado = models.CharField(max_length=15, choices=ESTADO, default=DISPONIBLE)
    espacio_especial = models.BooleanField(default=False)
    limpieza = models.BooleanField(default=False)  # Campo nuevo para requerir limpieza

    def __str__(self):
        return self.nombre

    REQUIRED_FIELDS = ['nombre', 'horario', 'descripcion',
                       'telefono', 'estado', 'espacio_especial', 'limpieza']

    def editar_espacio(self, nombre=None, horario=None, descripcion=None,
                       fotos=None, estado=None, telefono=None,
                       espacio_especial=None, limpieza=None):
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
        if espacio_especial is not None:
            self.espacio_especial = espacio_especial
        if limpieza is not None:
            self.limpieza = limpieza
        if telefono:
            self.telefono = telefono
        self.save()
        return self

    def borrar_espacio(self):
        self.delete()

    # Método para decodificar la imagen en Base64 (opcional)
    def get_decoded_image(self):
        if self.fotos:
            return base64.b64decode(self.fotos)
        return None
