from django import forms
from .models import EspacioPublico


class EspacioPublicoForm(forms.ModelForm):
    class Meta:
        model = EspacioPublico
        fields = ['nombre', 'horario', 'descripcion',
                  'fotos', 'telefono', 'estado']
