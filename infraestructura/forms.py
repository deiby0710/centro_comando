from django import forms
from .models import IncidenciaServidor, NodoServidor

class NodoServidorForm(forms.ModelForm):
    class Meta:
        model = NodoServidor
        fields = ['nombre_host', 'direccion_ip', 'motor_contenedores', 'proxy_inverso', 'en_produccion']

class IncidenciaServidorForm(forms.ModelForm):
    class Meta:
        model = IncidenciaServidor
        fields = ['titulo', 'descripcion', 'severidad', 'estado']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'severidad': forms.Select(attrs={
                'class': 'form-select'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
        }