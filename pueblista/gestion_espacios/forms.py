from django import forms
from gestion_reservas.models import Reserva
from .models import EspacioPublico


class EspacioPublicoForm(forms.ModelForm):
    class Meta:
        model = EspacioPublico
        fields = ['nombre', 'horario', 'descripcion', 'fotos', 'telefono', 'estado', 'espacio_especial', 'limpieza']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'horario': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control form-control-lg', 'pattern': r'^\d{9}$'}),
            'estado': forms.Select(attrs={'class': 'form-select form-select-lg'}),
            'fotos': forms.FileInput(attrs={'class': 'form-control form-control-lg'}),
            'espacio_especial': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'limpieza': forms.CheckboxInput(attrs={'class': 'form-check-input'}),  # Añadir este campo
            
        }


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
