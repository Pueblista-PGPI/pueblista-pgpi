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
    estado = models.CharField(
        max_length=30,
        choices=TIPOS_RESERVA,
        default=REALIZADA)
    espacio = models.ForeignKey(
        'gestion_espacios.EspacioPublico',
        on_delete=models.CASCADE, null=False, blank=False)

    usuario = models.ForeignKey('gestion_usuarios.CustomUser', on_delete=models.CASCADE, null=False, blank=False)
    # email = models.EmailField(max_length=100, null=False, blank=False)

    def __str__(self):
        return ("Espacio: " + self.espacio.nombre + " - Fecha: " + str(self.fecha) + 
            " - Desde: " + str(self.hora_inicio) + " Hasta: " + str(self.hora_fin) + 
            " - Estado: " + self.estado + " - Nombre: " + self.usuario.nombre + 
            " " + self.usuario.apellidos)
    
    class Meta:
        unique_together = ('espacio', 'fecha', 'hora_inicio')
        
    REQUIRED_FIELDS = ['fecha', 'hora_inicio', 'hora_fin', 'espacio', 'estado', 'usuario']
    
    def clean(self):
        # Validar que la hora de inicio sea menor que la hora de fin
        if self.hora_inicio and self.hora_fin and self.hora_inicio >= self.hora_fin:
            raise ValidationError('La hora de inicio debe ser menor que la hora de fin.')
        
        # Validar que la fecha no sea en el pasado
        if self.fecha and self.fecha < timezone.now().date():
            raise ValidationError('La fecha de la reserva no puede ser en el pasado.')
        
        # Validar que el espacio esté disponible
        if self.espacio.estado and self.espacio.estado == EspacioPublico.NO_DISPONIBLE:
            raise ValidationError('El espacio no está disponible para reservas.')

    def save(self, *args, **kwargs):
        self.full_clean()  # Llamar a full_clean para ejecutar las validaciones personalizadas
        super().save(*args, **kwargs)
    
    def modificar_reserva(self, fecha, hora_inicio, hora_fin, estado, espacio, usuario):
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.estado = estado
        self.espacio = espacio
        self.usuario = usuario
        self.save()

    def borrar_reserva(self):
        self.delete()