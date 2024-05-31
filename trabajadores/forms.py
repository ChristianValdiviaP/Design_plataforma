from django import forms
from .models import Trabajador, Documento
from .widgets import MultiFileInput

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['nombre', 'rut', 'cargo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.Select(attrs={'class': 'form-control'}),
        }

class MultiDocumentoForm(forms.Form):
    archivos = forms.FileField(widget=MultiFileInput(attrs={'class': 'form-control'}), required=True)
    fecha_emision = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=True)
    fecha_termino = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), required=True)

