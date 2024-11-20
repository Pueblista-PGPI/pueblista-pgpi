from django import forms
from gestion_reservas.models import Reserva
from .models import EspacioPublico


class EspacioPublicoForm(forms.ModelForm):
    class Meta:
        model = EspacioPublico
        fields = ['nombre', 'horario', 'descripcion',
                  'fotos', 'telefono', 'estado', 'espacio_especial']


class EstadoReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['estado']
        widgets = {
            'estado': forms.Select(choices=[
                ('Realizada', 'Realizada'),
                ('Cancelada', 'Cancelada'),
                ('En curso', 'En curso'),
                ('Finalizada', 'Finalizada')
            ])
        }
