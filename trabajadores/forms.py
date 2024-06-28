'''from django import forms
from .models import Trabajador, Documento
from multiupload.fields import MultiFileField

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['nombre', 'rut', 'cargo']

class DocumentoForm(forms.Form):
    archivos = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5)  
    fecha_emision = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    fecha_termino = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))'''

from django import forms
from .models import Trabajador, Documento

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['nombre', 'rut', 'cargo']

class DocumentoForm(forms.Form):
    archivo = forms.FileField(widget=forms.FileInput(attrs={'accept': '.pdf,.doc,.docx'}))
    fecha_emision = forms.DateField(widget=forms.SelectDateWidget)
    fecha_termino = forms.DateField(widget=forms.SelectDateWidget)

