from django import forms


class EspacioPublicoForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    horario = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea)
    fotos = forms.ImageField()
    telefono = forms.CharField(max_length=15, required=False)
    estado = forms.ChoiceField(choices=[
        ('reservado', 'Reservado'),
        ('libre', 'Libre'),
        ('no_disponible', 'No Disponible')
    ])
