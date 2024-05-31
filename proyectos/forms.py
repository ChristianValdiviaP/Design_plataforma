from django import forms
from .models import Proyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre_proyecto', 'nombre_faena']
        widgets = {
            'nombre_proyecto': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_faena': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RutForm(forms.Form):
    rut = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
