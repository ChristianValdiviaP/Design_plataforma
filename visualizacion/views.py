from django.shortcuts import render
from trabajadores.models import Trabajador
from proyectos.models import Proyecto

def buscar_trabajador(request):
    if request.method == 'POST':
        rut = request.POST.get('rut')
        try:
            trabajador = Trabajador.objects.get(rut=rut)
            proyectos = trabajador.proyectos.all()
            context = {
                'trabajador': trabajador,
                'proyectos': proyectos,
            }
            return render(request, 'visualizar/resultados.html', context)
        except Trabajador.DoesNotExist:
            return render(request, 'visualizar/buscar.html', {'error': 'Trabajador no encontrado'})
    return render(request, 'visualizar/buscar.html')
