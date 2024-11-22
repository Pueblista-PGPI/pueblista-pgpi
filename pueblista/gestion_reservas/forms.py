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
        
    def clean(self):
        cleaned_data = super().clean()
        hora_inicio = cleaned_data.get('hora_inicio')
        hora_fin = cleaned_data.get('hora_fin')

        if hora_inicio and hora_fin and hora_inicio >= hora_fin:
            raise forms.ValidationError('La hora de inicio no puede ser posterior o igual a la hora de fin.')

        return cleaned_data
