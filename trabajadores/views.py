'''from django.shortcuts import render, redirect
from django.views import View
from .forms import TrabajadorForm, DocumentoFormSet
from .models import Trabajador, Documento
from django.http import JsonResponse

class TrabajadorView(View):
    def get(self, request):
        trabajador_form = TrabajadorForm()
        documento_formset = DocumentoFormSet(queryset=Documento.objects.none())
        return render(request, 'trabajadores/trabajador_form.html', {
            'trabajador_form': trabajador_form,
            'documento_formset': documento_formset,
        })

    def post(self, request):
        trabajador_form = TrabajadorForm(request.POST)
        documento_formset = DocumentoFormSet(request.POST, request.FILES)

        if trabajador_form.is_valid() and documento_formset.is_valid():
            trabajador = trabajador_form.save()
            documentos = documento_formset.save(commit=False)
            for documento in documentos:
                documento.trabajador = trabajador
                documento.save()
            return redirect('trabajadores')

        return render(request, 'trabajadores/trabajador_form.html', {
            'trabajador_form': trabajador_form,
            'documento_formset': documento_formset,
        })
    
    def registrar_trabajador(request):
        if request.method == 'POST':
            trabajador_form = TrabajadorForm(request.POST)
            if trabajador_form.is_valid():
                trabajador = trabajador_form.save()
                archivos = request.FILES.getlist('archivo')
                fechas_emision = request.POST.getlist('fecha_emision')
                fechas_termino = request.POST.getlist('fecha_termino')

                for i, archivo in enumerate(archivos):
                    Documento.objects.create(
                        trabajador=trabajador,
                        archivo=archivo,
                        fecha_emision=fechas_emision[i],
                        fecha_termino=fechas_termino[i]
                    )

                return redirect('home')

        else:
            trabajador_form = TrabajadorForm()

        return render(request, 'trabajadores/trabajador_form.html', {
            'trabajador_form': trabajador_form
        })'''


from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Trabajador, Documento
from .forms import TrabajadorForm, DocumentoForm

def registrar_trabajador(request):
    if request.method == 'POST':
        trabajador_form = TrabajadorForm(request.POST)
        if trabajador_form.is_valid():
            trabajador = trabajador_form.save()
            archivos = request.FILES.getlist('archivo')
            fechas_emision = request.POST.getlist('fecha_emision')
            fechas_termino = request.POST.getlist('fecha_termino')

            for i, archivo in enumerate(archivos):
                Documento.objects.create(
                    trabajador=trabajador,
                    archivo=archivo,
                    fecha_emision=fechas_emision[i],
                    fecha_termino=fechas_termino[i]
                )

            return redirect('home')

    else:
        trabajador_form = TrabajadorForm()

    return render(request, 'trabajadores/trabajador_form.html', {
        'trabajador_form': trabajador_form
    })
