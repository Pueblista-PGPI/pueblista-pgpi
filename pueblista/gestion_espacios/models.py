from django.db import models


class EspacioPublico(models.Model):
    RESERVADO = "reservado"
    LIBRE = "libre"
    NO_DISPONIBLE = "no_disponible"

    ESTADO = [
        (RESERVADO, 'Reservado'),
        (LIBRE, 'Libre'),
        (NO_DISPONIBLE, 'No Disponible'),
    ]

    nombre = models.CharField(max_length=100)
    horario = models.CharField(max_length=100)
    descripcion = models.TextField()
    fotos = models.ImageField(upload_to='spaces',
                              verbose_name='photo', null=True, blank=True)
    telefono = models.CharField(max_length=15)
    estado = models.CharField(max_length=15, choices=ESTADO, default=LIBRE)

    def __str__(self):
        return self.nombre

    REQUIRED_FIELDS = ['nombre', 'horario', 'descripcion',
                       'telefono', 'estado']

    @classmethod
    def crear_espacio(self, nombre, horario, descripcion, fotos, estado=LIBRE,
                      telefono=None):

        if not nombre:
            raise ValueError('El nombre es obligatorio')
        if not horario:
            raise ValueError('Un horario es obligatorio')
        if not descripcion:
            raise ValueError('Una descripción es obligatoria')
        if not telefono:
            raise ValueError('El teléfono es obligatorio')

        espacio = self(
            nombre=nombre,
            horario=horario,
            descripcion=descripcion,
            fotos=fotos,
            estado=estado,
            telefono=telefono
        )
        espacio.save()
        return espacio

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
