from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect

def seleccionar_accion(request):
    if request.method == 'POST':
        if 'trabajador' in request.POST:
            return redirect('trabajadores')
        elif 'proyecto' in request.POST:
            return redirect('proyecto')
        elif 'visualizar' in request.POST:
            return redirect('visualizar_informacion')
    return render(request, 'home/home.html')

# home/views.py

from django.shortcuts import render
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request, 'home/home.html')
