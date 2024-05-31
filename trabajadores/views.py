from django.shortcuts import render, redirect
from .forms import TrabajadorForm, MultiDocumentoForm
from .models import Trabajador, Documento

def index(request):
    if request.method == 'POST':
        trabajador_form = TrabajadorForm(request.POST)
        documento_form = MultiDocumentoForm(request.POST, request.FILES)
        if trabajador_form.is_valid() and documento_form.is_valid():
            trabajador = trabajador_form.save()
            archivos = request.FILES.getlist('archivos')
            for archivo in archivos:
                Documento.objects.create(
                    trabajador=trabajador,
                    archivo=archivo,
                    fecha_emision=documento_form.cleaned_data['fecha_emision'],
                    fecha_termino=documento_form.cleaned_data['fecha_termino']
                )
            return redirect('ingresar_trabajador')
    else:
        trabajador_form = TrabajadorForm()
        documento_form = MultiDocumentoForm()

    documentos = Documento.objects.all()
    return render(request, 'trabajadores/index.html', {
        'trabajador_form': trabajador_form,
        'documento_form': documento_form,
        'documentos': documentos
    })

def eliminar_documento(request, id):
    documento = Documento.objects.get(id=id)
    documento.delete()
    return redirect('ingresar_trabajador')
