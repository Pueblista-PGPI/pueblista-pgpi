from django.db import models
from django.utils import timezone

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

    usuario = models.ForeignKey('gestion_usuarios.CustomUser', on_delete=models.CASCADE, null=False, blank=False)
    # email = models.EmailField(max_length=100, null=False, blank=False)

    def __str__(self):
        return ("Espacio: " + self.espacio.nombre + " - Fecha: " + str(self.fecha) + 
            " - Desde: " + str(self.hora_inicio) + " Hasta: " + str(self.hora_fin) + 
            " - Estado: " + self.estado + " - Nombre: " + self.usuario.nombre + 
            " " + self.usuario.apellidos)

    REQUIRED_FIELDS = ['fecha', 'hora_inicio', 'hora_fin', 'espacio', 'estado', 'usuario']

    def crear_reserva(self, fecha, hora_inicio, hora_fin, estado, espacio, usuario):
        if not Reserva.objects.filter(espacio=espacio, fecha=fecha, hora_inicio=hora_inicio).exists() and hora_inicio < hora_fin and fecha >= timezone.now().date():    
            self.fecha = fecha
            self.hora_inicio = hora_inicio
            self.hora_fin = hora_fin
            self.estado = estado
            self.espacio = espacio
            self.usuario = usuario
            self.save()
            return self
        else:
            return None

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
    
    
