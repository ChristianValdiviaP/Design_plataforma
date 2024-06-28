from django import forms
from .models import Proyecto, ProyectoTrabajadores
from trabajadores.models import Trabajador

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['nombre_proyecto', 'nombre_faena']

class TrabajadorSearchForm(forms.Form):
    search_query = forms.CharField(label='Buscar Trabajador', max_length=100)
