from django.db import models

# Create your models here.

class Notificacion(models.Model):
    
    fecha = models.DateTimeField(auto_now_add=True)
    mensaje = models.CharField(max_length=255)
    leida = models.BooleanField(default=False)
    usuario = models.ForeignKey('gestion_usuarios.CustomUser', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.mensaje
    
    class Meta:
        verbose_name = 'Notificación'
        verbose_name_plural = 'Notificaciones'
        ordering = ['-fecha']
        
    
    required_fields = ['mensaje', 'usuario']
        
        
    


