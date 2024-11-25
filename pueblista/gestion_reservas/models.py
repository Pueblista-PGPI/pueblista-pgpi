from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from gestion_espacios.models import EspacioPublico

# Create your models here.


class Reserva(models.Model):

    REALIZADA = 'Realizada'
    CANCELADA = 'Cancelada'
    EN_CURSO = 'En curso'
    FINALIZADA = 'Finalizada'

    TIPOS_RESERVA = [
        (REALIZADA, 'Realizada'),
        (CANCELADA, 'Cancelada'),
        (EN_CURSO, 'En curso'),
        (FINALIZADA, 'Finalizada'),
    ]

    fecha = models.DateField(null=False, blank=False)
    hora_inicio = models.TimeField(null=False, blank=False)
    hora_fin = models.TimeField(null=False, blank=False)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(
        max_length=30,
        choices=TIPOS_RESERVA,
        default=REALIZADA)
    espacio = models.ForeignKey(
        'gestion_espacios.EspacioPublico',
        on_delete=models.CASCADE, null=False, blank=False)
    subespacio = models.CharField(max_length=100, default="No procede")

    usuario = models.ForeignKey('gestion_usuarios.CustomUser',
                                on_delete=models.CASCADE, null=False,
                                blank=False)
    # email = models.EmailField(max_length=100, null=False, blank=False)

    def __str__(self):
        return ("Espacio: " + self.espacio.nombre +
                (" - Subespacio: " + self.subespacio
                 if self.subespacio != "No procede" else "") +
                " - Fecha: " + str(self.fecha) + " - Desde: " + 
                str(self.hora_inicio) + " Hasta: " + str(self.hora_fin) + " - Estado: " + self.estado
                + " - Nombre: " + self.usuario.nombre +
                " " + self.usuario.apellidos)

    class Meta:
        unique_together = ('espacio', 'subespacio', 'fecha', 'hora_inicio')

    REQUIRED_FIELDS = ['fecha', 'hora_inicio', 'hora_fin', 'espacio', 'estado', 'usuario']

    def clean(self):
        # Validar que la hora de inicio sea menor que la hora de fin
        if self.hora_inicio and self.hora_fin and self.hora_inicio >= self.hora_fin:
            raise ValidationError('La hora de inicio debe ser menor que la hora de fin.')

        # Validar que el espacio y el puesto (si aplica) esté disponible
        if Reserva.objects.filter(espacio=self.espacio,
                                  subespacio=self.subespacio,
                                  fecha=self.fecha,
                                  hora_inicio=self.hora_inicio).exists():
            if self.subespacio == "No procede":
                raise ValidationError('El espacio seleccionado no está disponible.')
            else:
                raise ValidationError('El espacio y puesto seleccionados no están disponibles.')
        
        # Validar que la fecha no sea en el pasado
        if self.fecha and self.fecha < timezone.now().date():
            raise ValidationError('La fecha de la reserva no puede ser en el pasado.')
        
        # Validar que el espacio esté disponible
        if self.espacio.estado and self.espacio.estado == EspacioPublico.NO_DISPONIBLE:
            raise ValidationError('El espacio no está disponible para reservas.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Llamar a full_clean para ejecutar las validaciones personalizadas
        super().save(*args, **kwargs)
    
    def modificar_reserva(self, fecha, hora_inicio, hora_fin, estado, espacio, subespacio, usuario):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.estado = estado
        self.espacio = espacio
        self.subespacio = subespacio
        self.usuario = usuario
        self.save()

    def borrar_reserva(self):
        self.delete()


class SolicitudReservaEspecial(models.Model):
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('CANCELADA', 'Cancelada'),
        ('ACEPTADA', 'Aceptada'),
    ]
    fecha = models.DateField(null=False, blank=False)
    hora_inicio = models.TimeField(null=False, blank=False)
    hora_fin = models.TimeField(null=False, blank=False)
    motivo = models.TextField(null=False, blank=False)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='PENDIENTE')
    motivo_cancelacion = models.TextField(blank=True, null=True)
    
    espacio = models.ForeignKey( 'gestion_espacios.EspacioPublico', on_delete=models.CASCADE, null=False, blank=False)
    usuario = models.ForeignKey('gestion_usuarios.CustomUser', on_delete=models.CASCADE, null=False, blank=False)
    
    def __str__(self):
        return ("Espacio: " + self.espacio.nombre + " - Fecha: " + str(self.fecha) + 
            " - Desde: " + str(self.hora_inicio) + " Hasta: " + str(self.hora_fin) + 
            " - Motivo: " + self.motivo + " - Nombre: " + self.usuario.nombre + 
            " " + self.usuario.apellidos)
        
    REQUIRED_FIELDS = ['fecha', 'hora_inicio', 'hora_fin', 'motivo', 'espacio', 'usuario']
    
    
