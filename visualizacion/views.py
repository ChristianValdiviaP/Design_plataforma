from django.shortcuts import render, redirect, get_object_or_404
from trabajadores.models import Trabajador, Documento
from proyectos.models import Proyecto, ProyectoTrabajadores
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

def visualizar_trabajadores(request):
    trabajadores_data = []
    
    # Obtener todos los trabajadores
    trabajadores = Trabajador.objects.all()
    
    # Iterar sobre los trabajadores y recopilar la información necesaria
    for trabajador in trabajadores:
        trabajador_proyectos = ProyectoTrabajadores.objects.filter(trabajador=trabajador)
        documentos_vencidos = Documento.objects.filter(trabajador=trabajador, fecha_termino__lt=timezone.now())
        
        for tp in trabajador_proyectos:
            proyecto = tp.proyecto
            trabajadores_data.append({
                'trabajador': trabajador,
                'nombre': trabajador.nombre,
                'cargo': trabajador.cargo.nombre,
                'nombre_proyecto': proyecto.nombre_proyecto,
                'nombre_faena': proyecto.nombre_faena,
                'documentos_vencidos': documentos_vencidos
            })
    
    context = {
        'trabajadores_data': trabajadores_data
    }
    
    return render(request, 'visualizar/visualizar_trabajadores.html', context)

def eliminar_documento(request, documento_id):
    documento = get_object_or_404(Documento, id=documento_id)
    documento.delete()
    return redirect('visualizar_trabajadores')

def subir_documento(request, trabajador_rut):
    if request.method == 'POST':
        trabajador = get_object_or_404(Trabajador, rut=trabajador_rut)
        archivo = request.FILES['archivo']
        fecha_emision = request.POST['fecha_emision']
        fecha_termino = request.POST['fecha_termino']
        
        # Guardar archivo en el sistema de archivos
        fs = FileSystemStorage()
        filename = fs.save(archivo.name, archivo)
        file_url = fs.url(filename)
        
        # Crear nuevo documento en la base de datos
        Documento.objects.create(
            trabajador=trabajador,
            archivo=file_url,
            fecha_emision=fecha_emision,
            fecha_termino=fecha_termino
        )
        return redirect('visualizar_trabajadores')
