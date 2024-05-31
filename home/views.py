from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

def seleccionar_accion(request):
    if request.method == 'POST':
        if 'trabajador' in request.POST:
            return redirect('ingresar_trabajador')
        elif 'proyecto' in request.POST:
            return redirect('ingresar_proyecto')
        elif 'visualizar' in request.POST:
            return redirect('visualizar_informacion')
    return render(request, 'home/seleccionar_accion.html')