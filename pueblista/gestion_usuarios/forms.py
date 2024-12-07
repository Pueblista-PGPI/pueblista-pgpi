from django import forms


class LoginForm(forms.Form):
    dni = forms.CharField(
        max_length=9,
        widget=forms.TextInput(attrs={'placeholder': '12345678A',
                                      'class': 'form-control'}),
        label="DNI"
    )
    fecha_nacimiento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date',
                                      'class': 'form-control'}),
        label="Fecha de nacimiento"
    )
