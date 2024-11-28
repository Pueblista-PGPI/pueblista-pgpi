from django import forms
from .models import AyuntamientoInfo

class AyuntamientoInfoForm(forms.ModelForm):
    class Meta:
        model = AyuntamientoInfo
        fields = ['titulo', 'descripcion', 'fotos']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'fotos': forms.FileInput(attrs={'class': 'form-control'}),
        }