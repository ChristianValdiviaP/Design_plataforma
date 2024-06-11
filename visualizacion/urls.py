from django.urls import path
from .views import buscar_trabajador

urlpatterns = [
    path('', buscar_trabajador, name='visualizar_informacion'),
]
