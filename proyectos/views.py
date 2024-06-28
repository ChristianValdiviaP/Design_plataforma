from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Proyecto, ProyectoTrabajadores
from .forms import ProyectoForm, TrabajadorSearchForm
from trabajadores.models import Trabajador

def crear_proyecto(request):
    if request.method == 'POST':
        proyecto_form = ProyectoForm(request.POST)
        search_form = TrabajadorSearchForm(request.POST)
        error_message = None

        # Recuperamos la lista de IDs de los trabajadores seleccionados de la sesión
        trabajadores_seleccionados = request.session.get('trabajadores_seleccionados', [])

        if 'buscar' in request.POST and search_form.is_valid():
            search_query = search_form.cleaned_data['search_query']
            trabajadores_encontrados = Trabajador.objects.filter(
                Q(rut__icontains=search_query) | Q(nombre__icontains=search_query)
            )
            if not trabajadores_encontrados:
                error_message = "No se encontraron trabajadores con los datos ingresados."
            else:
                error_message = None
                for trabajador in trabajadores_encontrados:
                    if trabajador.rut not in trabajadores_seleccionados:
                        trabajadores_seleccionados.append(trabajador.rut)

        elif 'guardar' in request.POST and proyecto_form.is_valid():
            proyecto = proyecto_form.save()
            for trabajador_id in trabajadores_seleccionados:
                trabajador = Trabajador.objects.get(rut=trabajador_id)
                # Verificar si ya existe el trabajador en el proyecto
                if not ProyectoTrabajadores.objects.filter(proyecto=proyecto, trabajador=trabajador).exists():
                    ProyectoTrabajadores.objects.create(proyecto=proyecto, trabajador=trabajador)
            # Limpiamos la lista de trabajadores seleccionados
            request.session['trabajadores_seleccionados'] = []
            return redirect('proyecto_exito')  # Redirigir a una página de éxito o a la lista de proyectos

        # Guardar la lista de trabajadores seleccionados en la sesión
        request.session['trabajadores_seleccionados'] = trabajadores_seleccionados
        trabajadores = Trabajador.objects.filter(rut__in=trabajadores_seleccionados)

    else:
        proyecto_form = ProyectoForm()
        search_form = TrabajadorSearchForm()
        trabajadores = []
        error_message = None
        request.session['trabajadores_seleccionados'] = []

    context = {
        'proyecto_form': proyecto_form,
        'search_form': search_form,
        'trabajadores': trabajadores,
        'error_message': error_message,
    }
    
    return render(request, 'proyectos/proyecto_form.html', context)
