from django import forms
from .models import SolicitudReservaEspecial

class SolicitudReservaEspecialForm(forms.ModelForm):
    class Meta:
        model = SolicitudReservaEspecial
        fields = ['fecha', 'hora_inicio', 'hora_fin', 'motivo', 'espacio', 'usuario']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe el motivo de la solicitud'}),
            'espacio': forms.HiddenInput(),  # Espacio oculto
            'usuario': forms.HiddenInput(),  # Usuario oculto
        }
        labels = {
            'fecha': 'Fecha de Reserva',
            'hora_inicio': 'Hora de Inicio',
            'hora_fin': 'Hora de Fin',
            'motivo': 'Motivo de la Solicitud',
        }