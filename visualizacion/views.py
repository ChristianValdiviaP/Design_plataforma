from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from trabajadores.models import Trabajador, Cargo
from proyectos.models import Proyecto

def visualizar_informacion(request):
    trabajadores = Trabajador.objects.all()
    cargos = Cargo.objects.all()
    proyectos = Proyecto.objects.all()
    return render(request, 'visualizacion/visualizar_informacion.html', {
        'trabajadores': trabajadores,
        'cargos': cargos,
        'proyectos': proyectos
    })
