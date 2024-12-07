from django.db import models

# Create your models here.
class AyuntamientoInfo(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fotos = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo