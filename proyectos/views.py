from django.shortcuts import render, redirect
from .forms import ProyectoForm, RutForm
from .models import Proyecto
from trabajadores.models import Trabajador, Documento

def proyectos_index(request):
    proyecto_form = ProyectoForm()
    rut_form = RutForm()
    trabajador = None
    documentos = []
    lista_informacion = request.session.get('lista_informacion', [])

    if request.method == 'POST':
        if 'buscar' in request.POST:
            rut_form = RutForm(request.POST)
            if rut_form.is_valid():
                rut = rut_form.cleaned_data['rut']
                try:
                    trabajador = Trabajador.objects.get(rut=rut)
                    documentos = Documento.objects.filter(trabajador=trabajador)
                except Trabajador.DoesNotExist:
                    trabajador = None
                    documentos = []
        
        elif 'agregar' in request.POST:
            rut = request.POST.get('rut')
            trabajador = Trabajador.objects.get(rut=rut)
            documento_ids = request.POST.getlist('documentos')
            documentos_seleccionados = Documento.objects.filter(id__in=documento_ids)
            info = {
                'rut': rut,
                'nombre_trabajador': trabajador.nombre,
                'documentos': [doc.id for doc in documentos_seleccionados],
                'documentos_nombres': [doc.archivo.name for doc in documentos_seleccionados],
            }
            lista_informacion.append(info)
            request.session['lista_informacion'] = lista_informacion

        elif 'subir' in request.POST:
            proyecto_form = ProyectoForm(request.POST)
            if proyecto_form.is_valid():
                proyecto = proyecto_form.save(commit=False)
                for info in lista_informacion:
                    trabajador = Trabajador.objects.get(rut=info['rut'])
                    proyecto.trabajador = trabajador
                    proyecto.save()
                    for doc_id in info['documentos']:
                        documento = Documento.objects.get(id=doc_id)
                        proyecto.documentos.add(documento)
                proyecto.save()
                request.session['lista_informacion'] = []

    context = {
        'proyecto_form': proyecto_form,
        'rut_form': rut_form,
        'trabajador': trabajador,
        'documentos': documentos,
        'lista_informacion': lista_informacion,
    }
    return render(request, 'proyectos/index.html', context)

def eliminar_info(request, index):
    lista_informacion = request.session.get('lista_informacion', [])
    if index < len(lista_informacion):
        del lista_informacion[index]
    request.session['lista_informacion'] = lista_informacion
    return redirect('proyectos_index')
