'''from django.shortcuts import render, redirect
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
    return redirect('ingresar_trabajador')'''


from django.shortcuts import render, redirect
from .forms import TrabajadorForm, DocumentoForm
from .models import Trabajador, Documento

def index(request):
    trabajador_form = TrabajadorForm()
    documento_form = DocumentoForm()
    lista_documentos = request.session.get('lista_documentos', [])

    if request.method == 'POST':
        if 'agregar' in request.POST:
            documento_form = DocumentoForm(request.POST, request.FILES)
            if documento_form.is_valid():
                archivos = request.FILES.getlist('archivos')
                fecha_emision = documento_form.cleaned_data['fecha_emision']
                fecha_termino = documento_form.cleaned_data['fecha_termino']
                
                for archivo in archivos:
                    lista_documentos.append({
                        'archivo': archivo.name,
                        'archivo_obj': archivo,
                        'fecha_emision': fecha_emision,
                        'fecha_termino': fecha_termino,
                    })
                
                request.session['lista_documentos'] = lista_documentos
                return redirect('trabajadores_index')

        elif 'subir' in request.POST:
            trabajador_form = TrabajadorForm(request.POST)
            if trabajador_form.is_valid():
                trabajador = trabajador_form.save()
                
                for doc_data in lista_documentos:
                    Documento.objects.create(
                        trabajador=trabajador,
                        archivo=doc_data['archivo_obj'],
                        fecha_emision=doc_data['fecha_emision'],
                        fecha_termino=doc_data['fecha_termino']
                    )
                
                request.session['lista_documentos'] = []
                return redirect('trabajadores_index')

    context = {
        'trabajador_form': trabajador_form,
        'documento_form': documento_form,
        'lista_documentos': lista_documentos,
    }
    return render(request, 'trabajadores/index.html', context)

def eliminar_documento(request, index):
    lista_documentos = request.session.get('lista_documentos', [])
    if 0 <= index < len(lista_documentos):
        del lista_documentos[index]
    request.session['lista_documentos'] = lista_documentos
    return redirect('trabajadores_index')
